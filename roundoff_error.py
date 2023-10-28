# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Bradley
# Section: ENGR-102-519
# Assignment: 4.17 LAB: Roundoff error
# Date: 9/11/23


############ Part A ############
a = 1 / 7
print(f"a = {a}")
b = a * 7
print(f"b = a * 7 = {b}")
# The value of b is 1 so there is no round-off
c = 2 * a
d = 5 * a
f = c + d
print(f"f = 2 * a + 5 * a = {f}")
# The value of f is not 1 so there is round-off
from math import sqrt
x = sqrt(1/3)
print(f"x = {x}")
y = x * x * 3
print(f"y = x * x * 3 = {y}")
# The value of y is 1 so there is no round-off
z = x * 3 * x
print(f"z = x * 3 * x = {z}")
# The value of z is not 1 so there is round-off

############ Part B ############

TOLERANCE = 1e-10
if abs(b - f) < TOLERANCE:
    print(f"b and f are equal within tolerance of {TOLERANCE}")
else:
    print(f"b and f are NOT equal within tolerance of {TOLERANCE}")
if abs(y - z) < TOLERANCE:
    print(f"y and z are equal within tolerance of {TOLERANCE}")
else:
    print(f"y and z are NOT equal within tolerance of {TOLERANCE}")

############ Part C ############

m = 0.1
print(f"m = {m}")
n = 3 * m
print(f"n = 3 * m = 0.3 {n==0.3}")
p = 7 * m
print(f"p = 7 * m = 0.7 {p==0.7}")
q = n + p
print(f"q = n + p = 1 {q==1}")