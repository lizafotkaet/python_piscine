#!/usr/bin/env python3

num1 = int(input("Enter the 1st num: "))
num2 = int(input("Enter the 2nd num: "))

mult = num1 * num2

print(f"{num1} x {num2} = {mult}")

if (mult > 0):
	print("The result is positive")
elif(mult < 0):
	print("The result is negative")
else:
	print("The result is zero")