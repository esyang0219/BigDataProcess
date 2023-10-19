#!/usr/bin/python3
def sale(p):
    return p*0.8
price = [10000, 8000, 7500, 12000, 25000]
for p in map(sale, price):
    print(p, end=', ')
print('\n')
