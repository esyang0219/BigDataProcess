#!/usr/bin/python3
import datetime
today = datetime.date.today()
birth = datetime.date(1994,5,5)
day = today - birth
print("%d days, 0:00:00" % day.days)
