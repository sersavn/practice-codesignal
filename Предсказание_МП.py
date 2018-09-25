'''
v3:

for_loop: +
added_reg: +


'''


'''
4. Создание набора данных для модели
'''
Name_Of_The_Current_Group = 'Тормозные камеры и энергоаккумуляторы' #название группы

import os
import re
import sys
import itertools
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from math import floor
from collections import OrderedDict
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

sns.set()
path = "K:\Отдел_снабжения\Сапрунов_Сергей\Предсказание_МП"
#savefig_path = "K:\Отдел_снабжения\Сапрунов_Сергей\Предсказание_Monthly_Demand\Картиночки"
files = os.listdir(path)
files_xlsx = [i for i in files if ".xlsx" in i]
print('')
# creating regex
r_AR = re.compile(".*AR")
r_BCD = re.compile(".*BCD")
r_SALES = re.compile(".*SALES")
r_assortment = re.compile(".*Ассортимент")
r_coefficients = re.compile(".*Коэффициенты")
r_REG = re.compile(".*REG")
# applying regex
AR_name = list(filter(r_AR.match, files_xlsx))[0]
BCD_name = list(filter(r_BCD.match, files_xlsx))[0]
SALES_name = list(filter(r_SALES.match, files_xlsx))[0]
assortment_name = list(filter(r_assortment.match, files_xlsx))[0]
coefficients_name = list(filter(r_coefficients.match, files_xlsx))[0]
# reading from xls
df_AR = pd.read_excel(path+'/'+AR_name)
df_BCD = pd.read_excel(path+'/'+BCD_name)
df_SALES = pd.read_excel(path+'/'+SALES_name)
df_assortment = pd.read_excel(path+'/'+assortment_name)
df_coefficients = pd.read_excel(path+'/'+coefficients_name)
#setting indexes
df_AR = df_AR.set_index(['Номенклатура', 'Склад'])
df_BCD = df_BCD.set_index(['Номенклатура', 'Склад'])
df_SALES = df_SALES.set_index(['Номенклатура', 'Склад'])
df_assortment = df_assortment.set_index('Номенклатура')
#taking assortment positions into account
df_assortment = df_assortment[df_assortment['Вид ассортимента'] == "Ассортимент"]
#group by "Номенклатура"
df_AR = df_AR.groupby(['Номенклатура']).agg('sum')
df_BCD = df_BCD.groupby(['Номенклатура']).agg('sum')
df_SALES = df_SALES.groupby(['Номенклатура']).agg('sum')
#inner horizontal concat in order to account only assortment positions
df_AR = pd.concat([df_AR, df_assortment], axis=1, join='inner')
df_BCD = pd.concat([df_BCD, df_assortment], axis=1, join='inner')
df_SALES = pd.concat([df_SALES, df_assortment], axis=1, join='inner')
#dropping assortment column
df_AR = df_AR.drop(['Вид ассортимента'], axis = 1)
df_BCD = df_BCD.drop(['Вид ассортимента'], axis = 1)
df_SALES = df_SALES.drop(['Вид ассортимента'], axis = 1)
#dealing with regs
REG_list = []
for i in list(filter(r_REG.match, files_xlsx)):
    REG_list.append(i)
df_list = []
for j in REG_list:
    aquired_df = pd.read_excel(path + '/' + j)
    aquired_df = aquired_df.set_index('номенклатура')
    df_list.append(aquired_df)
reg_df = pd.concat(df_list)
reg_df['ггод'] = reg_df['ггод'].astype(str)
reg_df['ггод'] = (reg_df['ггод'] + '-')
reg_df['ммесяц'] = reg_df['ммесяц'].astype(str)
reg_df['Date'] = reg_df['ггод'] + reg_df['ммесяц']
reg_df = reg_df.drop(['Товарная_Группа', 'ммесяц', 'ггод'], axis = 1)
reg_df['Date'] = pd.to_datetime(reg_df['Date'], errors='raise', format="%Y-%m", dayfirst=False, yearfirst=False)

def shape_checker():
    expression = df_AR.shape == df_BCD.shape == df_SALES.shape
    if expression != True:
        return sys.exit("Shapes of AR, BCD and ALES is not equal. Stopping")
    return "Shapes of AR, BCD and SALES are equal. Continuing"
print(shape_checker())
print('')

#pos_name = 'Тормозная камера с энергоаккумулятором без вилки тип 16/24 о.н. 544440020 (M2801624)'
pos_name = 'Тормозная камера с энергоаккумулятором с вилкой тип 24/30 о.н. 544420110 длинный шток (M2802430)'


dataframes_GroupedBy_Name = [df_AR, df_BCD, df_SALES]

def df_ColumnStr_to_datetime(DataFrame):
    try:
        DataFrame.columns = pd.to_datetime(DataFrame.columns.values, errors='raise', format="%d.%m.%Y %H:%M:%S", dayfirst=False, yearfirst=False)
    except:
        print("Months are written in russian again? Degenerati...")
        print("Nu nichego, prorvemsya!")
        print('---')
        months = {"Январь":"01.01", "Февраль":"01.02", "Март":"01.03", "Апрель":"01.04"
          , "Май":"01.05", "Июнь":"01.06", "Июль":"01.07", "Август":"01.08"
          , "Сентябрь":"01.09", "Октябрь":"01.10", "Ноябрь":"01.11", "Декабрь":"01.12"}
        new_month_names = []
        for i in DataFrame.columns.values:
            b = i.split(" ")[0]
            new_month_names.append(months[b])
        year_names = []
        for i in DataFrame.columns.values:
            b = i.split(" ")[1]
            year_names.append(b)
        full_new_name = [x +'.'+ y for x, y in zip(new_month_names, year_names)]
        #print(full_new_name)
        DataFrame.columns = full_new_name
        DataFrame.columns = pd.to_datetime(DataFrame.columns.values, errors='raise', format="%d.%m.%Y", dayfirst=False, yearfirst=False)
    return(DataFrame)

df_AR = df_ColumnStr_to_datetime(df_AR)
df_BCD = df_ColumnStr_to_datetime(df_BCD)
df_SALES = df_ColumnStr_to_datetime(df_SALES)

def reg_by_nom(nomenclature):
    reg_df_nom = reg_df
    reg_df_nom = reg_df_nom[reg_df_nom.index == nomenclature]
    reg_df_nom = reg_df_nom.sort_values(by=['Date'])
    reg_df_nom = reg_df_nom.set_index('Date')
    reg_df_nom = reg_df_nom.groupby('Date').sum()
    return reg_df_nom
def Nth_df_Full(nomenclature): #Неполный месяц!
    '''

    '''

    series_list = []
    for i in dataframes_GroupedBy_Name:
        series_list.append(i.loc[nomenclature])
    Npos_df = pd.concat(series_list, axis=1, sort=False)
    Npos_df.columns = ['AR', 'BCD', 'SALES']
    Npos_df = Npos_df[:-1]
    reg_df = reg_by_nom(nomenclature)
    nth_df = Npos_df
    merged_df = pd.concat([nth_df, reg_df], axis = 1)
    merged_df = merged_df.drop(['Количество'], axis = 1)
    merged_df['SALES_MA_12_MEAN'] = merged_df['SALES'].rolling(12).mean()
    merged_df = merged_df.rename({'Количество_Реализаций':'Operations'}, axis='columns')
    merged_df['Operations_MA_12_MEAN'] = merged_df['Operations'].rolling(12).mean()
    merged_df['AR_MA_12_MEAN'] = merged_df['AR'].rolling(12).mean()
    merged_df['BCD_MA_12_MEAN'] = merged_df['BCD'].rolling(12).mean()
    merged_df['Conversion'] = merged_df['Operations_MA_12_MEAN']/merged_df['AR_MA_12_MEAN']
    merged_df['Conversion'][merged_df['Conversion'] > 1]  = 1 #restricting conversion
    merged_df['Expected_Value'] = merged_df['SALES_MA_12_MEAN']/merged_df['Operations_MA_12_MEAN']
    merged_df['Monthly_Demand'] = merged_df['SALES'] + merged_df['BCD'] * merged_df['Conversion'] * merged_df['Expected_Value']
    merged_df['Demand_MA_12_MEAN'] = merged_df['SALES_MA_12_MEAN'] + merged_df['BCD_MA_12_MEAN'] * merged_df['Conversion'] * merged_df['Expected_Value']
    merged_df = merged_df.fillna(0)
    '''
    merged_df['Conversion'] - используются скользящие средние значения количества операций и AR запросов за 12 месяцев
    merged_df['Expected_Value'] - используются скользящие средние значения количества продаж и операций за 12 месяцев
    '''
    return merged_df
def Nth_df_Short(nomenclature):
    Short_df = Nth_df_Full(nomenclature)['Monthly_Demand'].to_frame()
    return Short_df
def heatmap_figure(DataFrame):
    plt.figure(figsize = (16,8))
    sns.heatmap(data = DataFrame, robust=False, linewidths=0, linecolor='white', annot = False)
    return plt.show()
def Nth_df_Figure(nomenclature):
    plt.figure(figsize=(21, 9))
    plt.plot(Nth_df_Full(nomenclature).index, 'AR', data = Nth_df_Full(nomenclature), alpha=1, ls = '--')
    plt.plot(Nth_df_Full(nomenclature).index, 'BCD', data = Nth_df_Full(nomenclature), alpha=1, ls = '--')
    plt.plot(Nth_df_Full(nomenclature).index, 'SALES', data = Nth_df_Full(nomenclature), ls = '--')
    plt.plot(Nth_df_Full(nomenclature).index, 'SALES_MA_12_MEAN', data = Nth_df_Full(nomenclature), linewidth = 2)
    plt.plot(Nth_df_Full(nomenclature).index, 'Monthly_Demand', data = Nth_df_Full(nomenclature), linewidth = 2)
    plt.plot(Nth_df_Full(nomenclature).index, 'Demand_MA_12_MEAN', data = Nth_df_Full(nomenclature), linewidth = 2)
    plt.title(str(nomenclature) + " *для конверсии и мат ожидания используются скользящие средние значения за последние 12 месяцев; Конверсия <= 1")
    Leg = plt.legend()
    Leg.get_texts()[3].set_text('Продажи скользящее среднее (Скользящее среднее по продажам за 12 месяцев)')
    Leg.get_texts()[4].set_text('Спрос')
    Leg.get_texts()[5].set_text('МП (Скользящее среднее по Спросу за 12 месяцев)')
    return plt.show()
def Nth_df_Distribution(nomenclature):
    plt.figure(figsize=(16, 8))
    sns.distplot(Nth_df_Full(nomenclature)['AR'], label='AR', hist=False, rug=False)
    sns.distplot(Nth_df_Full(nomenclature)['BCD'], label='BCD', hist=False, rug=False)
    sns.distplot(Nth_df_Full(nomenclature)['SALES'], label='SALES', hist=False, rug=False)
    sns.distplot(Nth_df_Full(nomenclature)['Monthly_Demand'], label='Monthly_Demand', hist=False, rug=False)
    plt.legend()
    return plt.show()
def Nth_df_Pairplot(nomenclature):
    sns.pairplot(Nth_df_Full(nomenclature))
    return plt.show()
def Seasonal_Coef(Group_Name, Seasonal_Cofficients_Sum):
    seasonal_coefficients = df_coefficients[df_coefficients['Группа номенклатуры'] == Group_Name]
    seasonal_coefficients = seasonal_coefficients.values[0][1:].tolist()
    if Seasonal_Cofficients_Sum == 12:
        seasonal_coefficients = [i - 0.1 for i in seasonal_coefficients]
    elif Seasonal_Cofficients_Sum == 13.2:
        pass
    else:
        sys.exit("Invalid Seasonal_Cofficients_Sum. Stopping")
    month_dict = dict(zip([i for i in range(1,13)], seasonal_coefficients))
    return month_dict
def Train_Test_Split_Indexes(nomenclature):
    TimeSeries = Nth_df_Short(nomenclature)
    Train_Test_Indexes_List = []
    rem = len(TimeSeries) % 12
    Num_of_TrainTest_sets = int((len(TimeSeries) - rem) / 12) - 1
    train_slice_first = 0
    for i in range(1, Num_of_TrainTest_sets + 1):
        train_slice_last = (rem + 12 * i)
        test_slice_first = (rem + 12 * i)
        test_slice_last = (rem + 12 * (i+1))
        Train_Test_Indexes_List.append([train_slice_first, train_slice_last, test_slice_first, test_slice_last])
    return Train_Test_Indexes_List
'''
Moving_Average_and_Stuff
'''
def MA(nomenclature):
    Nth_df_Short_nom = Nth_df_Short(nomenclature)
    Nth_df_Short_nom['MA_3_df_Monthly_Demand'] = Nth_df_Short_nom['Monthly_Demand'].rolling(window=3).mean()
    Nth_df_Short_nom['MA_3_forecast'] = Nth_df_Short_nom['MA_3_df_Monthly_Demand']
    Nth_df_Short_nom['MA_6_df_Monthly_Demand'] = Nth_df_Short_nom['Monthly_Demand'].rolling(window=6).mean()
    Nth_df_Short_nom['MA_6_forecast'] = Nth_df_Short_nom['MA_6_df_Monthly_Demand']
    Nth_df_Short_nom['MA_12_df_Monthly_Demand'] = Nth_df_Short_nom['Monthly_Demand'].rolling(window=12).mean()
    Nth_df_Short_nom['MA_12_forecast'] = Nth_df_Short_nom['MA_12_df_Monthly_Demand']
    for i in Train_Test_Split_Indexes(nomenclature):
        Nth_df_Short_nom.iloc[i[2]:i[3], 2] = Nth_df_Short_nom.iloc[(i[1]-1), 1]
        Nth_df_Short_nom.iloc[i[2]:i[3], 4] = Nth_df_Short_nom.iloc[(i[1]-1), 3]
        Nth_df_Short_nom.iloc[i[2]:i[3], 6] = Nth_df_Short_nom.iloc[(i[1]-1), 5]
    Nth_df_Short_nom.iloc[:Train_Test_Split_Indexes(nomenclature)[0][2], 2] = np.nan
    Nth_df_Short_nom.iloc[:Train_Test_Split_Indexes(nomenclature)[0][2], 4] = np.nan
    Nth_df_Short_nom.iloc[:Train_Test_Split_Indexes(nomenclature)[0][2], 6] = np.nan
    return Nth_df_Short_nom
def MA_w_seasonal_coef(nomenclature):
    Seasonal_Coef_Function_Result = Seasonal_Coef(Name_Of_The_Current_Group, 13.2)
    MA_result = MA(nomenclature)
    month_nums = [int(str(i)[5:7]) for i in MA_result.index]
    MA_result['Seasonal_Coefficient'] = [Seasonal_Coef_Function_Result[i] for i in month_nums]
    MA_result['MA_3_forecast'] = MA_result['MA_3_forecast'] * MA_result['Seasonal_Coefficient']
    MA_result['MA_6_forecast'] = MA_result['MA_6_forecast'] * MA_result['Seasonal_Coefficient']
    MA_result['MA_12_forecast'] = MA_result['MA_12_forecast'] * MA_result['Seasonal_Coefficient']
    return MA_result
def Mean_values(nomenclature):
    MA_w_seasonal_132 = MA_w_seasonal_coef(nomenclature)
    mean_vals = []
    for i in Train_Test_Split_Indexes(nomenclature):
        mean_vals.append([MA_w_seasonal_132.MA_12_df_Monthly_Demand[i[1]-1]]*12)
    return mean_vals
def MA_w_seasonal_coef_figure(nomenclature, number, show):
    Nth_df_Data_w_coef = MA_w_seasonal_coef(nomenclature)
    plt.figure(figsize=(21, 9))
    plt.plot(Nth_df_Data_w_coef.index, Nth_df_Data_w_coef['Monthly_Demand'], label = 'Real demand last 12 month')
    plt.plot(Nth_df_Data_w_coef.index, Nth_df_Data_w_coef['MA_3_forecast'], label = 'Predicted demand based on MA = 3', ls = '--', alpha=0.6)
    plt.plot(Nth_df_Data_w_coef.index, Nth_df_Data_w_coef['MA_6_forecast'], label = 'Predicted demand based on MA = 6', ls = '--', alpha=0.6)
    plt.plot(Nth_df_Data_w_coef.index, Nth_df_Data_w_coef['MA_12_forecast'], label = 'Predicted demand based on MA = 12', ls = '--', alpha=0.6, color = '#17becf')
    for num,val in enumerate(Train_Test_Split_Indexes(nomenclature)):
        plt.plot(Nth_df_Data_w_coef.index[(val[1]-12):val[1]], Mean_values(nomenclature)[num], ls = '-' , color = '#17becf', alpha=0.8, label = 'Trained sales based on MA = 12')
        plt.gca().axvline(x = Nth_df_Data_w_coef.index[(val[1])], ls = ':')
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = OrderedDict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys(), loc = 2)
    plt.xlim(xmin=Nth_df_Data_w_coef.index[0])
    plt.title(str(nomenclature) + " /" + " Добавить скрипт на классы (номенклатура)")
    plt.axvspan(Nth_df_Data_w_coef['Monthly_Demand'].index[Train_Test_Split_Indexes(nomenclature)[-1][2]], Nth_df_Data_w_coef['Monthly_Demand'].index[Train_Test_Split_Indexes(nomenclature)[-1][3]-1], alpha=0.5, color='white')
    plt.savefig(path + "/Картиночки/" + "MA_figure_Seasonal_coeff" + "_" + str(number) + ".png", dpi = 200)
    if show == True:
        return plt.show()
    elif show == False:
        return "MA_figure_Seasonal_coeff.png" + "_" + str(number) + " completed"
def MA_v2(nomenclature, rolling_attribute="Monthly_Demand", rolling_window=12, forecasting_horizon=12, with_seasonal_coef=True, offset=0):
    Nth_df_Short_nom = Nth_df_Short(nomenclature)[:len(Nth_df_Short(nomenclature))-offset]
    name = str(rolling_attribute) + '_rolling_' + str(rolling_window)
    Nth_df_Short_nom[name] = Nth_df_Short_nom[str(rolling_attribute)][:].rolling(window = rolling_window).mean()
    a = Nth_df_Short_nom.index[-1]
    b = Nth_df_Short_nom.index[-1] + pd.DateOffset(months=forecasting_horizon)
    #print(a,b)
    future_dates = []
    for i in range(1, forecasting_horizon+1):
        future_dates.append(a + pd.DateOffset(months=i))
    predicted_vals = Nth_df_Short_nom[name][-forecasting_horizon:]
    forecasting_df = pd.DataFrame({'date' : future_dates, 'predicted_vals' : predicted_vals})

    if with_seasonal_coef:
        Seasonal_Coef_Function_Result = Seasonal_Coef(Name_Of_The_Current_Group, 13.2)
        month_nums = [int(str(i)[5:7]) for i in forecasting_df['date']]
        forecasting_df['Seasonal_Coefficient'] = [Seasonal_Coef_Function_Result[i] for i in month_nums]
        forecasting_df['predicted_vals'] = forecasting_df['predicted_vals'] * forecasting_df['Seasonal_Coefficient']
        forecasting_df = forecasting_df.drop(['Seasonal_Coefficient'], axis = 1)
    return forecasting_df.set_index('date')
def MA_v2_figure(nomenclature, rolling_attribute="Monthly_Demand", rolling_window=12, forecasting_horizon=12, with_seasonal_coef=True, offset=0, number=0, show=False):
    #rolling_window = rolling_window+1 #BCS rolling window = 1 will initially do not give any prediction
    Nth_df_Short_nom = Nth_df_Short(nomenclature)#[:len(Nth_df_Short(nomenclature))-offset]
    name = str(rolling_attribute) + '_rolling_' + str(rolling_window)
    Nth_df_Short_nom[name] = Nth_df_Short_nom[str(rolling_attribute)][:].rolling(window = rolling_window).mean()

    MA_v2_result = MA_v2(nomenclature, rolling_attribute, rolling_window, forecasting_horizon, with_seasonal_coef, offset)

    plt.figure(figsize=(21, 9))
    plt.plot(Nth_df_Short_nom.index, Nth_df_Short_nom[name], linewidth = 2, label = 'Rolling_'+str(rolling_attribute)+'_'+str(rolling_window))
    plt.plot(Nth_df_Short_nom.index, Nth_df_Short_nom[rolling_attribute], linewidth = 2)

    mae = mean_absolute_error(Nth_df_Short_nom[rolling_attribute][rolling_window:], Nth_df_Short_nom[name][rolling_window:])
    deviation = np.std(Nth_df_Short_nom[rolling_attribute][rolling_window:] - Nth_df_Short_nom[name][rolling_window:])
    lower_bond = Nth_df_Short_nom[name] - (mae + 1.96 * deviation)
    upper_bond = Nth_df_Short_nom[name] + (mae + 1.96 * deviation)
    plt.plot(upper_bond, color = '#d62728', linewidth = 1.1, linestyle = '--', label = "Upper_Bond of CI for smoothed vals")
    plt.plot(lower_bond, color = '#d62728', linewidth = 1.1, linestyle = '--', label = "Lower_Bond of CI for smoothed vals")# IF C == 1.96

    lower_bond_vals = Nth_df_Short_nom[rolling_attribute][Nth_df_Short_nom[rolling_attribute] < lower_bond]
    upper_bond_vals = Nth_df_Short_nom[rolling_attribute][Nth_df_Short_nom[rolling_attribute] > upper_bond]
    plt.plot(upper_bond_vals, "ro", color = '#d62728', markersize = 10, label = "Anomalies")

    plt.plot(MA_v2_result.index, MA_v2_result['predicted_vals'], color = '#17becf', linestyle = '-.', label = 'MA_v2_result')
    plt.title("Moving Average\n Window Size = {} months\n Confidence = {}\n Nomenclature = {}".format(rolling_window,1.96,nomenclature))
    plt.legend()
    plt.savefig(path + "/Тест_моделей_для_предсказания_МП_графики/" +  "MA_v2_figure" + ".png", dpi = 200)
    return plt.show()
def MA_figure_anyParam(nomenclature, rolling_attribute, rolling_window, C = 1.96, plot_intervals=False, plot_anomalies=False):
    #rolling_window = rolling_window+1 #BCS rolling window = 1 will initially do not give any prediction
    Nth_df_Short_nom = Nth_df_Short(nomenclature)
    name = str(rolling_attribute) + '_rolling_' + str(rolling_window)
    Nth_df_Short_nom[name] = Nth_df_Short_nom[str(rolling_attribute)][:].rolling(window = rolling_window).mean()
    plt.figure(figsize=(21, 9))
    plt.plot(Nth_df_Short_nom.index, Nth_df_Short_nom[name], linewidth = 2, label = 'Rolling_'+str(rolling_attribute)+'_'+str(rolling_window))
    plt.plot(Nth_df_Short_nom.index, Nth_df_Short_nom[rolling_attribute], linewidth = 2)
    if plot_intervals:
        mae = mean_absolute_error(Nth_df_Short_nom['Monthly_Demand'][rolling_window:], Nth_df_Short_nom[name][rolling_window:])
        deviation = np.std(Nth_df_Short_nom['Monthly_Demand'][rolling_window:] - Nth_df_Short_nom[name][rolling_window:])
        lower_bond = Nth_df_Short_nom[name] - (mae + C * deviation)
        upper_bond = Nth_df_Short_nom[name] + (mae + C * deviation)
        plt.plot(upper_bond, color = '#d62728', linewidth = 1.1, linestyle = '--', label = "Upper_Bond of CI for smoothed vals")
        plt.plot(lower_bond, color = '#d62728', linewidth = 1.1, linestyle = '--', label = "Lower_Bond of CI for smoothed vals")# IF C == 1.96
    if plot_anomalies:
        lower_bond_vals = Nth_df_Short_nom['Monthly_Demand'][Nth_df_Short_nom['Monthly_Demand'] < lower_bond]
        upper_bond_vals = Nth_df_Short_nom['Monthly_Demand'][Nth_df_Short_nom['Monthly_Demand'] > upper_bond]
        plt.plot(upper_bond_vals, "ro", color = '#d62728', markersize = 10, label = "Anomalies")
    plt.title("Moving Average\n Window Size = {} months\n Confidence = {}\n Nomenclature = {}".format(rolling_window,C,nomenclature))
    plt.legend()
    plt.savefig(path + "/Тест_моделей_для_предсказания_МП_графики/" + "MA_figure_anyParam" + ".png", dpi = 200)
    return plt.show()
'''
Calculating errors for single position
'''
def Fact_vs_Prediction(nomenclature, model):
    Nth_df_result = Nth_df_Short(nomenclature)
    Combined_df = pd.concat([model, Nth_df_result], axis=1 , join = 'inner')
    return Combined_df
def MAPE(nomenclature, model):
    Fact_vs_Prediction_df = Fact_vs_Prediction(nomenclature, model)
    Fact_vs_Prediction_df['Value_Error'] = abs((Fact_vs_Prediction_df['Monthly_Demand'] - Fact_vs_Prediction_df['predicted_vals'])/Fact_vs_Prediction_df['Monthly_Demand'])
    #print(Fact_vs_Prediction_df)
    Fact_vs_Prediction_df
    return(1/len(Fact_vs_Prediction_df)*Fact_vs_Prediction_df['Value_Error'].sum())
def MAE(nomenclature, model):
    Fact_vs_Prediction_df = Fact_vs_Prediction(nomenclature, model)
    Fact_vs_Prediction_df['Value_Error'] = abs(Fact_vs_Prediction_df['Monthly_Demand'] - Fact_vs_Prediction_df['predicted_vals'])
    #print(Fact_vs_Prediction_df)
    Fact_vs_Prediction_df
    return(1/len(Fact_vs_Prediction_df)*Fact_vs_Prediction_df['Value_Error'].sum())
def AE(nomenclature, model):
    Fact_vs_Prediction_df = Fact_vs_Prediction(nomenclature, model)
    Fact_vs_Prediction_df['Value_Error'] = Fact_vs_Prediction_df['Monthly_Demand'] - Fact_vs_Prediction_df['predicted_vals']
    #print(Fact_vs_Prediction_df)
    Fact_vs_Prediction_df
    print('(Shortage_of_goods,', 'Surpulus_of_goods)')
    return(Fact_vs_Prediction_df['Value_Error'][Fact_vs_Prediction_df['Value_Error'] > 0].sum(), Fact_vs_Prediction_df['Value_Error'][Fact_vs_Prediction_df['Value_Error'] < 0].sum())
'''
Exponential_Smoothing_and_Stuff
'''

'''
ARIMA COMPONENTS
'''

def OLS_12(nomenclature):
    from sklearn import linear_model
    prediction_list = []
    trained_list = []
    lr_model = linear_model.LinearRegression()
    for i in Train_Test_Split_Indexes(nomenclature):
        X_train = np.asarray(list(range((i[1]-12), i[1]))).reshape(-1, 1)
        X_test = np.asarray(list(range(i[2], i[3]))).reshape(-1, 1)
        y_train = np.asarray(Nth_df_Short(nomenclature).SALES[(i[1]-12):i[1]]).reshape(-1, 1)
        fitted_model = lr_model.fit(X_train, y_train)
        train_sample = fitted_model.predict(X_train)
        trained_list.append(train_sample)
        prediction_sample = fitted_model.predict(X_test)
        prediction_list.append(prediction_sample)
    return trained_list,prediction_list
def OLS_12_w_seasonal_coef(nomenclature):
    Seasonal_Coefs_Extended = list(Seasonal_Coef(Name_Of_The_Current_Group, 12).values())*(len(Train_Test_Split_Indexes(nomenclature))+2) #'Sum_12' before
    Seasonal_Coefs_Extended_Slicded = []
    for j in Train_Test_Split_Indexes(nomenclature):
        Seasonal_Coefs_Extended_Slicded.append(Seasonal_Coefs_Extended[j[2]:j[3]])
    Seasonal_Coefs_Extended_Slicded_f = np.asarray(Seasonal_Coefs_Extended_Slicded).flatten()
    OLS_12_w_seasonal_f = np.asarray(OLS_12(nomenclature)[1]).flatten()
    OLS_12_w_seasonal_coef = [a*b for a,b in zip(Seasonal_Coefs_Extended_Slicded_f,OLS_12_w_seasonal_f)]
    return OLS_12_w_seasonal_coef #np.reshape(OLS_12_w_seasonal_coef, (-1, 4))
def OLS_12_w_seasonal_coef_figure(nomenclature, number, show):
    #Nth_df_Data_w_coef = MA_w_seasonal_coef(nomenclature)
    plt.figure(figsize=(21, 9))
    plt.plot(Nth_df_Full(nomenclature)['Monthly_Demand'].index, Nth_df_Full(nomenclature)['Monthly_Demand'], alpha=0.8, linewidth = 2)
    for num,val in enumerate(Train_Test_Split_Indexes(nomenclature)):
        plt.plot(Nth_df_Full(nomenclature)['Monthly_Demand'].index[val[2]:val[3]], OLS_12_w_seasonal_coef(nomenclature)[num*12:(num+1)*12], label = 'Predicted_Values', color = 'b', ls = '--', alpha=0.6)
        plt.plot(Nth_df_Full(nomenclature)['Monthly_Demand'].index[(val[1]-12):val[1]], OLS_12(nomenclature)[0][num], label = 'Trained_Values', color = 'm', ls = '-', alpha=0.8)
    for i in Train_Test_Split_Indexes(nomenclature):
        plt.gca().axvline(x = Nth_df_Full(nomenclature)['Monthly_Demand'].index[(i[1])], ls = ':')
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = OrderedDict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys(), loc = 2)
    plt.xlim(xmin=Nth_df_Full(nomenclature).index[0])
    plt.title(str(nomenclature) + " /" + " Добавить скрипт на классы (номенклатура)")
    plt.axvspan(Nth_df_Full(nomenclature)['Monthly_Demand'].index[Train_Test_Split_Indexes(nomenclature)[-1][2]], Nth_df_Full(nomenclature)['Monthly_Demand'].index[Train_Test_Split_Indexes(nomenclature)[-1][3]-1], alpha=0.5, color='white')
    plt.savefig(path + "/Картиночки/" + "OLS_figure_Seasonal_coeff" + "_" + str(number) + ".png", dpi = 200)
    if show == True:
        return plt.show()
    elif show == False:
        return "OLS_figure_Seasonal_coeff.png" + "_" + str(number) + " completed"
def HWModel_WO_CV(nomenclature):
    from statsmodels.tsa.holtwinters import ExponentialSmoothing
    Test = Nth_df_Full(nomenclature)['Monthly_Demand'].iloc[-12:]
    Train = Nth_df_Full(nomenclature)['Monthly_Demand'].iloc[:-12]
    model = ExponentialSmoothing(Train, seasonal = 'add', seasonal_periods = 12).fit()
    pred = model.predict(start = Test.index[0], end = Test.index[-1])
    return pred
def HWModel_W_CV(nomenclature):
    from statsmodels.tsa.holtwinters import ExponentialSmoothing
    prediction_list = []
    for i in Train_Test_Split_Indexes(nomenclature):
        Train = Nth_df_Full(nomenclature)['Monthly_Demand'][i[0]:i[1]]
        Test = Nth_df_Full(nomenclature)['Monthly_Demand'][i[2]:i[3]]
        model = ExponentialSmoothing(Train, seasonal = 'add', seasonal_periods = 12).fit()
        HoltWinters_predicted = model.predict(start=Test.index[0], end=Test.index[-1])
        prediction_list.append(HoltWinters_predicted)
    return prediction_list
def HWModel_W_CV_figure(nomenclature, number, show):
    plt.figure(figsize=(21, 9))
    plt.plot(Nth_df_Full(nomenclature)['Monthly_Demand'].index, Nth_df_Full(nomenclature)['Monthly_Demand'], alpha=0.8, linewidth = 2)
    for num,val in enumerate(Train_Test_Split_Indexes(nomenclature)):
        plt.plot(Nth_df_Full(nomenclature)['Monthly_Demand'].index[val[2]:val[3]], HWModel_W_CV(nomenclature)[num], label = 'Predicted_Values', color = 'b', ls = '--', alpha=0.6)
    for i in Train_Test_Split_Indexes(nomenclature):
        plt.gca().axvline(x = Nth_df_Full(nomenclature)['Monthly_Demand'].index[(i[1])], ls = ':')
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = OrderedDict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys(), loc = 2)
    plt.xlim(xmin=Nth_df_Full(nomenclature).index[0])
    plt.axvspan(Nth_df_Full(nomenclature)['Monthly_Demand'].index[Train_Test_Split_Indexes(nomenclature)[-1][2]], Nth_df_Full(nomenclature)['Monthly_Demand'].index[Train_Test_Split_Indexes(nomenclature)[-1][3]-1], alpha=0.5, color='white')#, color='lightgrey'
    plt.title(str(nomenclature) + " /" + " Добавить скрипт на классы (номенклатура)")
    plt.savefig(path + "/Картиночки/" + "OHW_W_CV_figure" + "_" + str(number) + ".png", dpi = 200)
    if show == True:
        return plt.show()
    elif show == False:
        return "HW_W_CV_figure.png" + "_" + str(number) + " completed"
def Supervised_df(nomenclature):
    Supervised_df = Nth_df_Full(nomenclature)#.copy(deep = True)
    year_list, month_list = [], []
    for i in Supervised_df.index.tolist():
        year_list.append(f"{i.year}")
        month_list.append(f"{i.month}")
    Supervised_df.reset_index(drop = True)
    Supervised_df['Year'] = year_list
    Supervised_df['Month'] = month_list
    Supervised_df = Supervised_df.reset_index()
    Supervised_df = Supervised_df.rename(columns={"index": "Date"})
    Supervised_df = Supervised_df.drop(columns = {"Date"})
    Supervised_df['Months'] = [i for i in range(len(Supervised_df))]
    '''
    Dropping all MA vals
    '''
    #Supervised_df = Supervised_df.drop(['SALES_MA_12_MEAN', 'Operations_MA_12_MEAN', 'AR_MA_12_MEAN', 'BCD_MA_12_MEAN', 'Demand_MA_12_MEAN', 'Expected_Value', 'Conversion', 'Operations', 'BCD', 'AR', 'SALES', 'Year'], axis = 1)
    print(Supervised_df)
    return Supervised_df
def Supervised_df_Pairplot(nomenclature):
    plt.figure(figsize=(21, 9))
    sns.pairplot(Supervised_df(nomenclature))
    plt.savefig(path + "/" + "Supervised_df_Pairplot" + ".png", dpi = 200)
    return plt.show()
def XGBoost_regression(nomenclature):
    from sklearn.ensemble import GradientBoostingRegressor
    predicted_values_list = []
    for num,val in enumerate(Train_Test_Split_Indexes(nomenclature)):
        train = Supervised_df(nomenclature)[val[0]:val[1]]
        test = Supervised_df(nomenclature)[val[2]:val[3]]
        X_train = train[train.columns.difference(['Monthly_Demand'])]
        y_train = train['Monthly_Demand']
        X_test = test[test.columns.difference(['Monthly_Demand'])]
        y_test = test['Monthly_Demand']
        model = GradientBoostingRegressor()
        fitted_model = model.fit(X_train, y_train)
        y_predicted = fitted_model.predict(X_test)
        predicted_values_list.append(y_predicted)
    return predicted_values_list
def XGBoost_figure(nomenclature, number, show):
    plt.figure(figsize=(21, 9))
    plt.plot(Nth_df_Full(nomenclature)['Monthly_Demand'].index, Nth_df_Full(nomenclature)['Monthly_Demand'], alpha=0.8, linewidth = 2)
    for num,val in enumerate(Train_Test_Split_Indexes(nomenclature)):
        plt.plot(Nth_df_Full(nomenclature)['Monthly_Demand'].index[val[2]:val[3]], XGBoost_regression(nomenclature)[num], label = 'Predicted_Values', color = 'b', ls = '--', alpha=0.6)
    for i in Train_Test_Split_Indexes(nomenclature):
        plt.gca().axvline(x = Nth_df_Full(nomenclature)['Monthly_Demand'].index[(i[1])], ls = ':')
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = OrderedDict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys(), loc = 2)
    plt.xlim(xmin=Nth_df_Full(nomenclature).index[0])
    plt.axvspan(Nth_df_Full(nomenclature)['Monthly_Demand'].index[Train_Test_Split_Indexes(nomenclature)[-1][2]], Nth_df_Full(nomenclature)['Monthly_Demand'].index[Train_Test_Split_Indexes(nomenclature)[-1][3]-1], alpha=0.5, color='white')
    plt.title(str(nomenclature) + " /" + " Добавить скрипт на классы (номенклатура)")
    plt.savefig(path + "/Картиночки/" + "XGBoost_figure" + "_" + str(number) + ".png", dpi = 200)
    if show == True:
        return plt.show()
    elif show == False:
        return "XGBoost_figure.png" + "_" + str(number) + " completed"
def NN_regression(nomenclature):
    from sklearn.neural_network import MLPRegressor
    predicted_values_list = []
    for num,val in enumerate(Train_Test_Split_Indexes(nomenclature)):
        train = Supervised_df(nomenclature)[val[0]:val[1]]
        test = Supervised_df(nomenclature)[val[2]:val[3]]
        X_train = train[train.columns.difference(['Monthly_Demand'])]
        y_train = train['Monthly_Demand']
        X_test = test[test.columns.difference(['Monthly_Demand'])]
        y_test = test['Monthly_Demand']
        model = MLPRegressor(solver = 'lbfgs', shuffle = False, max_iter = 500)
        fitted_model = model.fit(X_train, y_train)
        y_predicted = fitted_model.predict(X_test)
        predicted_values_list.append(y_predicted)
    return predicted_values_list
def NN_regression_figure(nomenclature, number, show):
    plt.figure(figsize=(21, 9))
    plt.plot(Nth_df_Full(nomenclature)['Monthly_Demand'].index, Nth_df_Full(nomenclature)['Monthly_Demand'], alpha=0.8, linewidth = 2)
    for num,val in enumerate(Train_Test_Split_Indexes(nomenclature)):
        plt.plot(Nth_df_Full(nomenclature)['Monthly_Demand'].index[val[2]:val[3]], NN_regression(nomenclature)[num], label = 'Predicted_Values', color = 'b', ls = '--', alpha=0.6)
    for i in Train_Test_Split_Indexes(nomenclature):
        plt.gca().axvline(x = Nth_df_Full(nomenclature)['Monthly_Demand'].index[(i[1])], ls = ':')
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = OrderedDict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys(), loc = 2)
    plt.xlim(xmin=Nth_df_Full(nomenclature).index[0])
    plt.axvspan(Nth_df_Full(nomenclature)['Monthly_Demand'].index[Train_Test_Split_Indexes(nomenclature)[-1][2]], Nth_df_Full(nomenclature)['Monthly_Demand'].index[Train_Test_Split_Indexes(nomenclature)[-1][3]-1], alpha=0.5, color='white')
    plt.title(str(nomenclature) + " /" + " Добавить скрипт на классы (номенклатура)")
    plt.savefig(path + "/Картиночки/" + "NN_figure" + "_" + str(number) + ".png", dpi = 200)
    if show == True:
        return plt.show()
    elif show == False:
        return "NN_figure.png" + "_" + str(number) + " completed"
def initial_data(nomenclature):
    real_values = []
    for i in Train_Test_Split_Indexes(Nth_df_Full(nomenclature)['Monthly_Demand']):
        real_values.append(Supervised_df(nomenclature)['Monthly_Demand'][i[2]:i[3]])
    return real_values
'''
OPTIONAL FUNCTIONS
'''
def picture_loop():
    for num,value in enumerate(df_AR.index[:]):
        MA_w_seasonal_coef_figure(value, num, False)
        OLS_12_w_seasonal_coef_figure(value, num, False)
        HWModel_W_CV_figure(value, num, False)
        XGBoost_figure(value, num, False)
        NN_regression_figure(value, num, False)
    return 'Done'
def confidence_interval(nomenclature):
    from scipy.stats import sem, t
    from scipy import mean
    confidence = 0.95
    SALES_data = Nth_df_Short(nomenclature)["SALES"][-12:]
    l = len(SALES_data)
    m = mean(SALES_data)
    std_err = sem(SALES_data)
    h = std_err * t.ppf((1 + confidence)/2, l-1)
    return (m-h), (m+h)
'''
ANALYZING RESULTS
'''
list_of_models = [MA, MA_w_seasonal_coef, HWModel_WO_CV, XGBoost_regression, NN_regression]

def Sales_per_pos():
    total_sales = []
    for i in df_AR.index[:]:
        sales_last_12month = (sum(Nth_df_Short(i)[-12:].values).tolist())[0]
        total_sales.append(sales_last_12month)
    return total_sales
def output_correcter(model, nomenclature):
    if model == MA or model == MA_w_seasonal_coef: #1d numpy.ndarray
        return (model(nomenclature)['MA_12_forecast'].values).tolist() #1d list
    elif model == OLS_12_w_seasonal_coef:
        predicted_vals = model(nomenclature)
        return predicted_vals
    elif model == HWModel_WO_CV:
        predicted_vals = model(nomenclature).values.tolist()
        return predicted_vals
    elif model == XGBoost_regression or model == NN_regression:
        predicted_vals = (np.asarray(model(nomenclature)).reshape(-1,)).tolist()
        return predicted_vals
def MSE_last_12_month(model):
    Model_MSE = []
    for i in df_AR.index[:]:
        predicted_output = output_correcter(model, i)[-12:]
        real_output = (Nth_df_Short(i)[-12:].values).tolist()
        Position_MSE = mean_squared_error(real_output,predicted_output)
        Model_MSE.append(Position_MSE)
    return Model_MSE
def df_MSE_last_12_month(model_list):
    pos_names = [i for i in df_AR.index[:]]
    df = pd.DataFrame(index = pos_names)
    for models in model_list:
        model_results = MSE_last_12_month(models)
        df[str(models)] = model_results
    return df
    #writer = pd.ExcelWriter('MSE_last_12_month.xlsx')
    #df.to_excel(writer,'Sheet1')
    #writer.save()
    #return 'MSE_last_12_month.xlsx Done!'

'''
PRINTING EVERYTHING
'''

#print(reg_df.index)
#print(reg_df)
#print()
#print(reg_by_nom(pos_name))
#print(Nth_df_Full(pos_name))#.loc['2017-07-01']
#print(heatmap_figure(df_SALES))
#print(Nth_df_Short(pos_name))
#print(Nth_df_Figure(pos_name))
#print(Nth_df_Distribution(pos_name))
#print(Nth_df_Pairplot(pos_name))
#print(Train_Test_Split_Indexes(pos_name))
#print(MA(pos_name))
#print(MA_w_seasonal_coef(pos_name))
#print(Mean_values(pos_name))
#print(MA_w_seasonal_coef_figure(pos_name, 1, False))
#print(HWModel_WO_CV(pos_name))
#print(HWModel_W_CV(pos_name))
#print(Supervised_df(pos_name))
#print(Supervised_df_Pairplot(pos_name))
#print(df_AR.index)
#print(Supervised_df_Pairplot(pos_name))
#print(XGBoost_regression(pos_name))
#print(XGBoost_figure(pos_name,1,True))
#print(NN_regression(pos_name))
#print(NN_regression_figure(pos_name,1,True))
#print(Sales_per_pos(), len())
