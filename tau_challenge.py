# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Bradley
# Section: ENGR-102-519
# Assignment: 3.19.1: LAB: Challenge program
# Date: 8/31/23

import math
digits = int(input("Please enter the number of digits of precision for tau: "))
#Syntax is goofy
print(f"The value of tau to {digits} digits is: {math.tau:.{digits}f}")