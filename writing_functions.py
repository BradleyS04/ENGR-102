# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Bradley
# Section: ENGR-102-519
# Assignment: 3.18.1: LAB: Writing functions
# Date: 8/31/23

import math
side = float(input("Please enter the side length: "))
def triangle(side):
    area = (math.sqrt(3)/4)*(side**2)
    return area
def square(side):
    area = (side * side)
    return area
def pentagon(side):
    area = .25*(math.sqrt(5*(5+(2*math.sqrt(5)))))*(side**2)
    return area
def dodecagon(side):
    area = 3 * (2 + math.sqrt(3)) * (side**2)
    return area
#These are my print statement
print(f"A triangle with side {side:.2f} has area {triangle(side):.3f}")
print(f"A square with side {side:.2f} has area {square(side):.3f}")
print(f"A pentagon with side {side:.2f} has area {pentagon(side):.3f}")
print(f" A dodecagon with side {side:.2f} has area {dodecagon(side):.3f}")