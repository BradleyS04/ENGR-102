# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Long Vo
#               Bradley Sun
#               Liam Searing
#
# Section:      519
# Assignment:   6.11 LAB: Pyramid area (part 1)
# Date:         9/25/23
# totalArea += (3 * ((length * layer) * length)) * ((sqrt(3) * (length * layer) ** 2) / 4)
from math import *
length = float(input("Enter the side length in meters: "))
layer = int(input("Enter the number of layers: "))
totalArea = 0
while (layer > 0):
    totalArea += ((layer * 3) * (length ** 2) + (layer ** 2) * ((sqrt(3) * length ** 2) / 4)) - (((layer - 1) ** 2) * ((sqrt(3) * length ** 2) / 4))
    layer -= 1
print(f"You need {totalArea:.2f} m^2 of gold foil to cover the pyramid")