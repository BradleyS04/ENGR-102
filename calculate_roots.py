# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Bradley
# Section: ENGR-102-519
# Assignment: 4.19 LAB: Calculate roots
# Date: 9/11/23

from math import *
a = float(input("Please enter the coefficient A: "))
b = float(input("Please enter the coefficient B: "))
c = float(input("Please enter the coefficient C: "))
#This checks the validity of the coefficients
if (a == 0 and b == 0 and c != 0):
    print("You entered an invalid combination of coefficients!")
    exit()
if (a == 0):
    print(f"The root is x = {-c/b}")
    exit()
if ((b ** 2) - 4 * a * c) < 0:
    num = abs((abs((b ** 2) - 4 * a * c))/2*a)
    if (num > abs(b) and num%b == 0):
        imaginary = str((((b ** 2) - 4 * a * c) / -2 * a)/b)
        b/=b
    elif (num < abs(b) and b%num == 0):
        imaginary = str((((b ** 2) - 4 * a * c) / -2 * a) / num)
        b/=num
    else:
        imaginary = str(((b**2)-4*a*c)/-2*a)
    imaginary += "i"
    print(f"The roots are x = {-b} + {imaginary} and x = {-b} - {imaginary}")
    exit()
root1 = -1*(b + sqrt((b**2)-4*a*c))/(2*a)
root2 = -1*(b - sqrt((b**2)-4*a*c))/(2*a)
if (root1 == root2):
    print(f"The root is x = {root1}")
elif (root1>root2):
    print(f"The roots are x = {root1} and x = {root2}")
else:
    print(f"The roots are x = {root2} and x = {root1}")