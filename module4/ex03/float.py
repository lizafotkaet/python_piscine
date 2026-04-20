#!/usr/bin/env python3

num = float(input("Enter a number: "))

test = int(num)

# if (num == test):
# 	print("Number is an integer")
# else:
# 	print("Number is a decimal")

if num.is_integer():
	print("Num is an int")
else:
	print("Num is a decimal")
