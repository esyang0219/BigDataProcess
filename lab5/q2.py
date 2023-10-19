#!/usr/bin/python3
a = []
b = []
for i in range(11):
    a.append(i)
    b.append(i ** 2)
dic = dict(zip(a, b))
print(dic[6])
