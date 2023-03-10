#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Get the last number by taking the mod
abs = number % 10
if abs > 5:
    print(f"Last digit of {number} is {abs} and is greater than 5")
elif abs == 0:
    print(f"Last digit of {number} is {abs} and is 0")
elif abs < 6:
    print(f"Last digit of {number} is {abs} and is less than 6 and not 0")
