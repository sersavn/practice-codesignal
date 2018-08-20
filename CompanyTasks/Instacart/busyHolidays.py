shoppers = [["10:00","11:00"],
 ["10:00","11:00"],
 ["12:00","13:00"],
 ["12:00","13:00"]]
orders = [["10:00","11:00"],
 ["10:00","11:00"],
 ["10:00","11:00"],
 ["12:00","13:00"]]
leadTime = [5, 5, 5, 5]

import numpy as np

def busyHolidays(shoppers, orders, leadTime):

    def get_min(time_str):
            h, m = time_str.split(':')
            return (int(h) * 60 + int(m))

    deliveries = []
    for otime,interval in zip(orders,leadTime):
        for stime in shoppers:
            possibility = [] # one of the delivery option
            possibility.append(otime)
            possibility.append(stime)
            possibility.append(interval)
            deliveries.append(possibility)
    print(deliveries)

    TimeList = []
    for e in deliveries:
        matchWindowStart = max(e[0][0],e[1][0])
        matchWindowEnd = min(e[0][1],e[1][1])
        TimeWindow = (get_min(matchWindowEnd) - get_min(matchWindowStart))
        TimeCheck = (TimeWindow - e[2])
        TimeList.append(TimeCheck)

    print(TimeList)

    norders = len(orders)
    t = [TimeList[i:i+norders] for i in range(0, len(TimeList), norders)]
    print('t', t)

    #Checking that courier is making single delivery
    check1 = [e for e in t]
    check1 = np.array(check1)
    check2 = np.rot90(check1)

    print('check1', check1)
    print('check2', check2)
    for i in check1:
        if max(i) < 0:
            return False
    for i in check2:
        if max(i) < 0:
            return False

    return True
