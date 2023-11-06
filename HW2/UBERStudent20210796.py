#!/usr/bin/python3
import sys
import calendar

def information(line):
	info=line.strip().split(',')
	base_num, date, vehicles, trips=info
	month,day,year=date.split('/')
	return base_num, month, day, year, vehicles, trips

def write_info(input_file, output_file):
	with open(input_file, 'r') as f1, open(output_file, 'w') as f2:
		for line in f1:
			base_num,month,day,year,vehicles,trips=information(line)
			dayofweek=['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
			eng_day=calendar.weekday(int(year), int(month), int(day))
			f2.write(f"{base_num},{dayofweek[eng_day]} {vehicles},{trips}\n")
if __name__ == '__main__':
	input_file=sys.argv[1]
	output_file=sys.argv[2]
	write_info(input_file, output_file)
