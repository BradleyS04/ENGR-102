# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Bradley
# Section: ENGR-102-519
# Assignment: 6.13 LAB: Howdy Whoop
# Date: 9/25/23
int1 = int(input("Enter an integer: "))
int2 = int(input("Enter another integer: "))
#This is my for loop
for i in range(1, 101):
    if (i%int1 == 0 and i%int2 == 0):
        print("Howdy Whoop")
        continue
    if (i%int1 == 0):
        print("Howdy")
        continue
    if (i%int2 == 0):
        print("Whoop")
        continue
    else:
        print(i)
