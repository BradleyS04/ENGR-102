# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Bradley
# Section: ENGR-102-519
# Assignment: 4.16 LAB: Largest number
# Date: 9/11/23

#This finds the largest number from three inputs
num1 = float(input("Enter number 1: "))
largestNum = num1
num2 = float(input("Enter number 2: "))
if (num2 > largestNum):
    largestNum = num2
num3 = float(input("Enter number 3: "))
if (num3 > largestNum):
    largestNum = num3
print(f"The largest number is {largestNum}")
