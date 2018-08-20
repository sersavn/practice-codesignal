'''
You just bought a public transit card that allows you to ride the Metro for a certain number of days.

Here is how it works: upon first receiving the card, the system allocates you a 31-day pass, which equals the number of days in January.
The second time you pay for the card, your pass is extended by 28 days,
i.e. the number of days in February (note that leap years are not considered), and so on.
The 13th time you extend the pass, you get 31 days again.

You just ran out of days on the card, and unfortunately you've forgotten how many times your pass has been extended so far.
However, you do remember the number of days you were able to ride the Metro during this most recent month.
Figure out the number of days by which your pass will now be extended, and return all the options as an array sorted in increasing order.

Example

For lastNumberOfDays = 30, the output should be
metroCard(lastNumberOfDays) = [31].
'''

from calendar import monthrange

def metroCard(lastNumberOfDays):
    MonthDays = [monthrange(2019, d)[1] for d in range(1,13)]
    MonthDays = list(enumerate(MonthDays))

    AnswerList = [MonthDays[e-1][1] for e in range(1,len(MonthDays)) if MonthDays[e][1] == lastNumberOfDays]

    #for e in range(1,len(MonthDays)):
    #    if MonthDays[e][1] == lastNumberOfDays:
    #        AnswerList.append(MonthDays[e-1][1])

    return list(set(AnswerList))
