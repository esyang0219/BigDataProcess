#!/usr/bin/python3
import sys
from datetime import datetime

def info(input_file, output_file):
	uberDict = dict()
	with open(input_file, 'r') as f:
		for line in f:
			line = line.strip()
			fields = line.split(',')
			region = fields[0]
			dateString = fields[1]
			vehicles = int(fields[2])
			trips = int(fields[3])
			date = datetime.strptime(dateString, "%m/%d/%Y")
			dayofweek=['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
			day = dayofweek[date.weekday()]

			uberKey = "%s,%s" % (region, day)
			if uberKey in uberDict:
				uberDict[uberKey][0] += vehicles
				uberDict[uberKey][1] += trips
			else:
				uberDict[uberKey] = [vehicles, trips]
	with open(output_file, 'w') as f:
		for uberKey, uberValue in uberDict.items():
			f.write("%s %d,%d\n" % (uberKey, uberValue[0], uberValue[1]))

if __name__ == '__main__':
	input_file=sys.argv[1]
	output_file=sys.argv[2]
	info(input_file, output_file)
