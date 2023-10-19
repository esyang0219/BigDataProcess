#!/usr/bin/python3
file_name = input('Enter file name : ')
f = open(file_name)

sender_dict = dict()
for line in f:
    line = line.strip()
    if line.startswith("From: "):
        strarr = line.split()
        sender_id = strarr[1]
        if sender_id in sender_dict:
            sender_dict[sender_id] += 1
        else:
            sender_dict[sender_id] = 1
print(sender_dict)
