import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

date_of_birthday = dt.datetime(year=1994, month=12, day=31, hour=4)
print(date_of_birthday)
