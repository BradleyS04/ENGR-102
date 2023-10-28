# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Bradley
# Section: ENGR-102-519
# Assignment: 4.18 LAB: How many gadgets
# Date: 9/11/23

#This is my factory
days = int(input("Please enter a positive value for day: "))
gadgets = 3820
if(days < 0):
    print("You entered an invalid number!")
    exit()
elif(days < 11):
    gadgets = days*10
elif(days < 51):
    gadgets = int((days**2/2) + (days/2) + 45)
elif(days<101):
    gadgets = (days*50)-1180
print(f"The sum total number of gadgets produced on day {days} is {gadgets}")