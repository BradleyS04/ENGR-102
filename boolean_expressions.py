# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Long Vo
#               Bradley Sun
#               Liam Searing
#
# Section:      519
# Assignment:   4.15 LAB: Boolean expressions
# Date:         9/11/23
#
############ Part A ############
a = input("Enter True or False for a: ")
if(a == "f" or a=="F" or a=="False"):
    a = False
else:
    a = True
b = input("Enter True or False for b: ")
if(b == "f" or b=="F" or b=="False"):
    b = False
else:
    b = True
c = input("Enter True or False for c: ")
if(c == "f" or c=="F" or c=="False"):
    c = False
else:
    c = True
############ Part B ############
print(f"a and b and c: {bool(a and b and c)}")
print(f"a or b or c: {bool(a or b or c)}")
############ Part C ############
print(f"XOR: {bool(a and (not b)) or ((not a) and b)}")
print(f"Odd number: {bool(((not((a and (not b)) or (not a) and b)) and c) or ((not c) and ((a and (not b)) or ((not a) and b))))}")
############ Part D ############
print(f"Complex 1: {(not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)}")
print(f"Complex 2: {(not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))}")
print(f"Simple 1: {(not a and b and not c) or (a and not b)}")
print(f"Simple 2: {((c and (not b or a)) or (a and not c))}")