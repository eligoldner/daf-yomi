import datetime
from zmanim.limudim.calculators.daf_yomi_bavli import DafYomiBavli
# from zmanim import hebrew_calendar -- want to print Hebrew date as well

today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
oneWeek = today - datetime.timedelta(days = 7)
OneMonth = today - datetime.timedelta(days = 30)
threeMonths = today - datetime.timedelta(days = 90)

daf = DafYomiBavli()
daf1 = daf.limud(today).description()
daf2 = daf.limud(yesterday).description()
daf3 = daf.limud(oneWeek).description()
daf4 = daf.limud(OneMonth).description()
daf5 = daf.limud(threeMonths).description()

# print(today.strftime('%B %d, %Y') & " Today's daf is: " & DafYomiBavli().limud(today))
print(f"Today, {today.strftime('%B %d, %Y')}, the daf is: {daf1}")
print(f"Yesterday's daf is: {daf2}")
print(f"Last week's daf is: {daf3}")
print(f"Last Month's daf is: {daf4}")
print(f"Last Quarters's daf is: {daf5}")

# want to limit the above to the 14th+ cycle, need to find it