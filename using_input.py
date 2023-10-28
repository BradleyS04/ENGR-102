# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Bradley
# Section: ENGR-102-519
# Assignment: 3.17.1: LAB: Using input
# Date: 8/31/23

import math
#This is my math
print("This program calculates the applied force given mass and acceleration")
mass = float(input("Please enter the mass (kg): "))
accel = float(input("Please enter the acceleration (m/s^2): "))
print(f"Force is {mass*accel:.1f} N")
print("This program calculates the wavelength given distance and angle")
dist = float(input("Please enter the distance (nm): "))
angle = float(input("Please enter the angle (degrees): "))
print(f"Wavelength is {(2*(dist*(math.sin((angle*math.pi)/180)))):.4f} nm")
print("This program calculates how much Radon-222 is left given time and initial amount")
time = float(input("Please enter the time (days): "))
initial = float(input("Please enter the initial amount (g): "))
print(f"Radon-222 left is {initial*(2**(-time/3.8)):.2f} g")
print("This program calculates the pressure given moles, volume, and temperature")
moles = float(input("Please enter the number of moles: "))
volume = float(input("Please enter the volume (m^3): "))
temp = float(input("Please enter the temperature (K): "))
print(f"Pressure is {((moles*8.314*temp)/volume)/1000:.0f} kPa")