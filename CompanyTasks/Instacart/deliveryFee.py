'''
To make sure that groceries can always be delivered,
Instacart tries to equally distribute delivery requests throughout the day by including an additional delivery fee during busy periods.

Each day is divided into several intervals that do not overlap and cover the whole day from 00:00 to 23:59.
For each i the delivery fee in the intervals[i] equals fees[i].

Given the list of delivery requests deliveries, your task is to check whether the delivery fee is directly correlated to the order volume in each interval
i.e. the interval_fee / interval_deliveries value is constant for each interval throughout the day.

Example

For
intervals = [0, 10, 22], fees = [1, 3, 1] and

deliveries = [[8, 15],
              [12, 21],
              [15, 48],
              [20, 17],
              [23, 43]]
the output should be
deliveryFee(intervals, fees, deliveries) = true.

The day is divided into 3 intervals:

from 00:00 to 09:59, the first delivery was made, fees[0] / 1 = 1;
from 10:00 to 21:59, the 2nd, 3rd and 4th deliveries were made, fees[1] / 3 = 1;
from 22:00 to 23:59, the last delivery was made, fees[2] / 1 = 1.
interval_fee / interval_deliveries = 1 for each interval, so the answer is true.
'''

def deliveryFee(intervals, fees, deliveries):

    intervals.append(24)
    deliveriesShort = [i[0] for i in deliveries]
    answerlist = []

    for i in range(len(intervals)-1):
        meter = 0
        for delivery in deliveriesShort:
            if intervals[i] <= delivery < intervals[i+1]:
                meter += 1
        answerlist.append(meter)

    try:
        dividingLists = [b / m for b,m in zip(answerlist, fees)]
        return len(set(dividingLists)) == 1
    except:
        return False
