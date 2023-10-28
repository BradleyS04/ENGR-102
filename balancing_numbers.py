# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Bradley
# Section: ENGR-102-519
# Assignment: 6.16 LAB: Balancing numbers
# Date: 9/25/23
n = int(input("Enter a value for n: "))
printn = n
sum = 0
r = 0
counter = 0
for i in range(1, n):
    sum += i
#checks the possibility of n being a balanced number
while (r < sum):
    n += 1
    r += n
    counter += 1
    if(r == sum):
        print(f"{printn} is a balancing number with r ={counter}")
        exit()
print(f"{printn} is not a balancing number")

