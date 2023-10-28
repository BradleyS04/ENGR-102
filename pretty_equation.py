# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Long Vo
#               Bradley Sun
#               Liam Searing
#
# Section:      519
# Assignment:   4.14 LAB: Pretty equation
# Date:         9/11/23
#

#Coding
a = int(input("Please enter the coefficient A: "))
b = int(input("Please enter the coefficient B: "))
c = int(input("Please enter the coefficient C: "))
part1 = ""
part2 = ""
part3 = ""
if (a == -1):
    a = str("- ")
    part1 = a+"x^2"
elif (a == 1):
    part1 = "x^2"
elif(a < 0):
    a = str(f"- {abs(a)}")
    part1 = a+"x^2"
elif(a > 0):
    a = str(a)
    part1 = a + "x^2"

if (b == -1):
    b = str(" - ")
    part2 = b+"x"
elif (b == 1):
    if(a==0):
        part2 = "x"
    else:
        part2 = " + x"
elif(b < 0):
    b = str(f" - {abs(b)}")
    part2 = b+"x"
elif(b > 0):
    if(a==0):
        part2 = str(b) + "x"
    else:
        b = str(b) + "x"
        part2 = str(f" + {b}")

if (c < 0):
    part3 = str(f" - {abs(c)}")
elif (c > 0):
    part3 = str(f" + {c}")
print(f"The quadratic equation is {part1+part2+part3} = 0")
