# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Bradley
# Section: ENGR-102-519
# Assignment: 2.10 LAB: More Linear Interpolation
# Date: 8/23/23
slopeX = (-5-8)/(85-12)
slopeY = (30-6)/(85-12)
slopeZ = (9-7)/(85-12)
start = 30.0
#This iterates through 30 seconds to 60 seconds
for i in range(5):
    print("At time",start,"seconds:")
    x1 = (slopeX * (start-12))+8
    print(f"x{i+1} = {x1} m")
    y1 = (slopeY * (start-12))+6
    print(f"y{i + 1} = {y1} m")
    z1 = (slopeZ * (start-12))+7
    print(f"z{i + 1} = {z1} m")
    if (i != 4):
        print("-----------------------")
    start += 7.5