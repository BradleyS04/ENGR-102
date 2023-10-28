# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Bradley
# Section: ENGR-102-519
# Assignment: 3.15 LAB: Unit Conversions
# Date: 8/30/23

x = float(input("Please enter the quantity to be converted:"))
# These are my functions
def newtons(input):
    input*=4.44822
    return input
def feet(input):
    input*=3.28084
    return input
def atm(input):
    input*=101.325
    return input
def watt(input):
    input*=3.412142
    return input
def litre(input):
    input*=15.850323140625001
    return input
def celsius(input):
    input = (input*(9/5))+32
    return input
print(f"{x:.2f} pounds force is equivalent to {newtons(x):.2f} Newtons")
print(f"{x:.2f} meters is equivalent to {feet(x):.2f} feet")
print(f"{x:.2f} atmospheres is equivalent to {atm(x):.2f} kilopascals")
print(f"{x:.2f} watts is equivalent to {watt(x):.2f} BTU per hour")
print(f"{x:.2f} liters per second is equivalent to {litre(x):.2f} US gallons per minute")
print(f"{x:.2f} degrees Celsius is equivalent to {celsius(x):.2f} degrees Fahrenheit")
