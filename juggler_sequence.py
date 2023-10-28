# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Bradley
# Section: ENGR-102-519
# Assignment: 6.15 LAB: Juggler sequence
# Date: 9/25/23
from math import *
counter = 0
num = int(input("Enter a positive integer: "))
print(f"The Juggler sequence starting at {num} is:")
print(f"{num}", end="")
while (num != 1):
    #Check if even
    if(num%2 == 0):
        num = floor(sqrt(num))
        counter += 1
        print(f", {num}", end = "")
    else:
        num = floor(num ** (3/2))
        counter += 1
        print(f", {num}", end = "")
print()
print(f"It took {counter} iterations to reach 1")