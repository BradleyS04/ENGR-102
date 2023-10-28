# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Bradley
# Section: ENGR-102-519
# Assignment: 3.16 LAB: Still More Linear Interpolation
# Date: 8/30/23

time1 = float(input("Enter time 1:"))
x1 = float(input("Enter the x position of the object at time 1:"))
y1 = float(input("Enter the y position of the object at time 1:"))
z1 = float(input("Enter the z position of the object at time 1:"))
time2 = float(input("Enter time 2:"))
x2 = float(input("Enter the x position of the object at time 2:"))
y2 = float(input("Enter the y position of the object at time 2:"))
z2 = float(input("Enter the z position of the object at time 2:"))
print(f"At time {time1:.2f} seconds the object is at ({x1:.3f}, {y1:.3f}, {z1:.3f})")
#slope function
interval = (time2-time1)/4
slopeX = (x2-x1)/(time2-time1)
slopeY = (y2-y1)/(time2-time1)
slopeZ = (z2-z1)/(time2-time1)
tempTime = time1
for i in range(3):
    tempTime += interval
    print(f"At time {tempTime:.2f} seconds the object is at ({(slopeX*(tempTime-time1))+x1:.3f}, {(slopeY*(tempTime-time1))+y1:.3f}, {(slopeZ*(tempTime-time1))+z1:.3f})")

print(f"At time {time2:.2f} seconds the object is at ({x2:.3f}, {y2:.3f}, {z2:.3f})")
"""
#This calculates if a number is a PDI or not given a number and power

number = int(input("Enter a 4-digit integer: "))

#store this number to check with the result

check1 = number

power = int(input("Enter the power: "))

#isolate thousands place

thousand = number // 1000

number -= thousand * 1000

#isolate hundreds place

hundred = number // 100

number -= hundred * 100

#isolate tens place

tens = number // 10

number -= tens * 10

ones = number

#Doing the calculation to check with "check1"

check2 = (thousand ** power) + (hundred ** power) + (tens ** power) + (ones ** power)

if (check == check1):

    print(f"{number} with given power {power} is a PDI")

else:

    print(f"{number} with given power {power} is NOT a PDI")
"""