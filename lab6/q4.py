#!/usr/bin/python3
try:
    num1, num2 = map(int, input("숫자 두 개를 입력하세요 : ").split())
    result = float(num1/num2)
    print(result)
except:
    print("division by zero")
