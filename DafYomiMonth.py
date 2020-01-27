from datetime import timedelta, date, time 
from zmanim.limudim.calculators.daf_yomi_bavli import DafYomiBavli 

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

daf = DafYomiBavli()
start_date = date(2020, 1, 5)
end_date = date(2020, 1, 31)
LearningItems = []

# startTime = time()

for Daf4Day in daterange(start_date, end_date):
    today = Daf4Day
    yesterday = today - timedelta(days = 1)
    oneWeek = today - timedelta(days = 7)
    OneMonth = today - timedelta(days = 30)
    threeMonths = today - timedelta(days = 90)

    LearningToday = today, daf.limud(today).description(), daf.limud(yesterday).description(),daf.limud(oneWeek).description(),daf.limud(OneMonth).description(),daf.limud(threeMonths).description()
    LearningItems.append(LearningToday)

print (LearningItems)

# endTime = time()
# elapsedTime = endTime - startTime
print (f'Start time {startTime}, End Time {endTime}')#, elapsed time {elapsedTime}')