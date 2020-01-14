import datetime
from zmanim.limudim.calculators.daf_yomi_bavli import DafYomiBavli
# from zmanim import hebrew_calendar -- want to print Hebrew date as well

today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
oneWeek = today - datetime.timedelta(days = 7)
OneMonth = today - datetime.timedelta(days = 30)
threeMonths = today - datetime.timedelta(days = 90)
# htoday = hebrew_calendar.jewish_date.date(today)
# limud = DafYomiBavli().limud(today)


# print(today.strftime('%B %d, %Y') & " Today's daf is: " & DafYomiBavli().limud(today))
print(f"Today, {today.strftime('%B %d, %Y')}, the daf is: {DafYomiBavli().limud(today).description()}")
print(f"Yesterday's daf is: {DafYomiBavli().limud(yesterday).description()}")
print(f"Last week's daf is: {DafYomiBavli().limud(oneWeek).description()}")
print(f"Last Month's daf is: {DafYomiBavli().limud(OneMonth).description()}")
print(f"Last Quarters's daf is: {DafYomiBavli().limud(threeMonths).description()}")

# want to limit the above to the 14th+ cycle, need to find it