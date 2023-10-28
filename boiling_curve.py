# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Bradley
# Section: ENGR-102-519
# Assignment: 5.4 LAB: Boiling curve
# Date: 9/20/23
from math import *
flux = 0
heat = float(input("Enter the excess temperature: "))
#Create slope1 with points (1.3, 1000) and (5, 7000)
slope1 = (log10(7000/1000))/(log10(5/1.3))
#Create slope2 with points (5, 7000) and (30, 1.5 * 10^6)
slope2 = (log10((1.5 * (10**6))/7000)/(log10(30/5)))
#Create slope3 with points (30, 1.5 * 10^6) and (120, 2.5 * 10^4)
slope3 = (log10((2.5 * (10**4))/(1.5 * (10**6))))/(log10(120/30))
#Create slope4 with points (120, 2.5 * 10^4) and (1200, 1.5 * 10^6)
slope4 = (log10((1.5 * (10**6))/(2.5 * (10**4))))/(log10(1200/120))
#checks if slope 1 is used
if(1.3 <= heat <= 5):
    #calculates flux with slope1
    flux = 1000*((heat/1.3)**slope1)
#checks if slope 2 is used
elif(5 < heat <= 30):
    #calculates flux with slope2
    flux = 7000*((heat/5)**slope2)
#Checks if slope 3 is used
elif(30 <  heat <= 120):
    #calculates flux with slope3
    flux = (1.5 * (10**6))*((heat/30)**slope3)
#checks if slope 4 is sued
elif(120 < heat <= 1200):
    #calculates flux with slope4
    flux = (2.5 * (10**4))*((heat/120)**slope4)
else:
    #Otherwise, the heat is outside of the domain
    #Which makes it extrapolation and return with
    #not available and exit the program
    print("Surface heat flux is not available")
    exit()
#Formatted string to print surface heat flux
print(f"The surface heat flux is approximately {flux:.0f} W/m^2")