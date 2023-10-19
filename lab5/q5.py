#!/usr/bin/python3
import json

with open('movies.json') as datafile:
    jsondata = json.load(datafile)

movies = list(jsondata['boxOfficeResult']['dailyBoxOfficeList'])

total = 0
for movie in movies:
    total += int(movie['salesAmt'])

print("오늘 매출액은 총 %d 원" % total)
