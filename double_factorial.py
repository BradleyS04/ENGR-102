# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Bradley
# Section: ENGR-102-519
# Assignment: 6.14 LAB: Double factorial
# Date: 9/25/23
def doublefactorial(num):
    result = 1
    #This checks if num is valid or not
    if(num <= 0):
        return 1
        exit()
    while num > 0:
        result *= num
        num -= 2
    return result