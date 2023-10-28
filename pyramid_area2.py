# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Long Vo
#               Bradley Sun
#               Liam Searing
#
# Section:      519
# Assignment:   6.12 LAB: Pyramid area (part 2)
# Date:         9/25/23
from math import *
# Variables
length = float(input("Enter the side length in meters: "))
layer = float(input("Enter the number of layers: "))
# Calc
totalArea = 1
def notaloop(layer):
    if layer == 1:
        return (3 * (length ** 2)) + (sqrt(3) / 4 * (length ** 2))
    else:
        return ((layer * 3) * (length ** 2) + (layer ** 2) * ((sqrt(3) * length ** 2) / 4)) - (((layer - 1) ** 2) * ((sqrt(3) * length ** 2) / 4)) + notaloop(layer - 1)
print(f"You need {notaloop(layer):.2f} m^2 of gold foil to cover the pyramid")
