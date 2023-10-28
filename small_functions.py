# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Bradley
# Section: ENGR-102-519
# Assignment: 9.16.1: LAB: Small functions
# Date: 10/23/23

from math import *

def parta(sphere_radius, hole_radius):
    #calculates sphere volume
    sphere_volume = (4 / 3) * pi * (sphere_radius ** 3)
    #find the height of the cylinder using pythag thm
    h = sqrt((sphere_radius**2)-(hole_radius**2))
    #finds volume of cylinder
    cylindrical_volume = 2 * (pi * (hole_radius**2) * h)
    #finds volume of hemisphere
    hemisphere_volume = ((1/3) * pi * (sphere_radius-h)) * (3*(hole_radius**2) + ((sphere_radius-h) ** 2))
    #subtract cylinder and hemisphere volume from the sphere
    bead_volume = sphere_volume - cylindrical_volume - hemisphere_volume
    return bead_volume

#print(parta(1,0.25))
def partb(n):
    #Creates empty variables
    list_output = []
    temp = 0
    #for loop to check adjacent numbers
    for i in range (1, n , 2):
        for j in range (i, n, 2):
            #checks if the numbers add to n
            temp += j
            list_output.append(j)
            if (temp == n):
                return list_output
        #resets the variables if they do not meet
        temp = 0
        list_output = []
    #returns false if nothing is met
    return False
#print(partb(4))

def partc(char, name, company, email):
    #builds the max length
    max_length = max(len(name), len(company), len(email)) + 2
    #creates a border for the top and bottom
    border = str(char) * (max_length + 4)
    #adds everything out in a string with new line
    contact_info = f"{border}\n{char} {name:^{max_length}} {char}\n{char} {company:^{max_length}} {char}\n{char} {email:^{max_length}} {char}\n{border}"
    return contact_info
#print(partc('*', 'Dr. Ritchey', 'Texas A&M University', 'snritchey@tamu.edu'))

def partd(num_list):
    #sorts and creates an empty list
    num_list.sort()
    output_list = []
    #checks if the list is even or odd to determine what math to do on median
    if len(num_list)%2 == 0:
        #math for even lists
        index1 = int(len(num_list)/2)
        num1 = num_list[index1]
        index2 = (int(len(num_list) / 2))-1
        num2 = num_list[index2]
        avg = (num1 + num2) / 2
    else:
        #math for odd lists
        avg = num_list[int((len(num_list)/2)-.5)]
    #appends the calculated values into the output
    output_list.append(num_list[0])
    output_list.append(avg)
    output_list.append(num_list[-1])
    return tuple(output_list)
#print(partd([1,3,2,4]))

def parte(time_list, distance_list):
    #creates empty list for output
    output_list = []
    #for loop to get the velocity
    for i in range(len(distance_list)-1):
        output_list.append(distance_list[i+1]-distance_list[i])
    return output_list
#print(parte([0, 1, 2, 3], [0, 1, 4, 9]))

def partf(num_list):
    for i in num_list:
        for j in num_list:
            #double for loop to check if any values add to 2027
            if (i+j == 2027):
                #if so, return the product of the two numbers
                return (i*j)
    #if not, then return false
    return False
#print(partf([1149, 5926, 1111, 2222, 3333, 916, 5555]))

def partg(x, tolerance):
    #creats a sum and n for iteration
    sum = 0
    n = 1
    #did a while loop for this, but a for loop works too
    while(True):
        #math with the formula to check and add to sum
        eval = (2/((2*n)-1)) * (x**((2*n)-1))
        #checks if the evaluation is under the tolerance, if so, return the sum
        if (abs(eval) < abs(tolerance)):
            return sum
        #otherwise, add eval to sum and iterate n
        sum += eval
        n += 1
#print(partg(-0.5, 1e-8))