# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Bradley
# Section: ENGR-102-519
# Assignment: 1.13: LAB: Follow Directions
# Date: 8/21/23

from math import *
#This program models the limit of a function
print("This shows the evaluation of sin(x-1)/(x-1) evaluated close to x=1")
print("My guess is 1")
x = 1.1
Result = (sin(x-1))/(x-1)
print(Result)
x = 1.01
Result = (sin(x-1))/(x-1)
print(Result)
x = 1.001
Result = (sin(x-1))/(x-1)
print(Result)
x = 1.0001
Result = (sin(x-1))/(x-1)
print(Result)
x = 1.00001
Result = (sin(x-1))/(x-1)
print(Result)
x = 1.000001
Result = (sin(x-1))/(x-1)
print(Result)
x = 1.0000001
Result = (sin(x-1))/(x-1)
print(Result)
x = 1.00000001
Result = (sin(x-1))/(x-1)
print(Result)
print()
print("My guess was correct")