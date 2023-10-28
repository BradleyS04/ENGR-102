# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Long Vo
#               Bradley Sun
#               Liam Searing
#
# Section:      519
# Assignment:   Lab 2.8.1
# Date:         30/08/2023
#

import math

r = 6745

t0 = 10.0
t2 = 55.0

dist0 = 2027.0
dist2 = 23027.0

slope = (dist2 - dist0) / (t2 - t0)

t1 = 25
pos = slope * (t1 - t0) + dist0

print("Part 1:")
print("For t =", t1, "minutes, the position p =", pos, "kilometers")

#part 2

t1 = 300
pos = slope * (t1 - t0) + dist0
pos = pos % (2 * math.pi * r)

print("Part 2:")
print("For t =", t1, "minutes, the position p =", pos, "kilometers")
