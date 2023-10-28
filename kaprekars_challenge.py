# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Bradley
# Section: ENGR-102-519
# Assignment: 7.29 LAB: Kaprekar's constant challenge
# Date: 10/5/23
total = 0
for i in range(10000):
    # ask user for input
    number = i

    # initialize the constants
    counter = 0
    current_num = number
    end = 6174

    # run loop until it reaches the end number (also check for 0)
    while (current_num != end) and (current_num != 0):
        # convert the number to a list
        num_string = str(current_num)
        while len(num_string) < 4:
            num_string = '0' + num_string
        num_list = [int(num) for num in num_string]

        # sort the lists both ways
        ascending = sorted(num_list)
        descending = sorted(num_list, reverse=True)

        # convert the lists to numbers
        ascending_num = ""
        for num in ascending:
            ascending_num += str(num)
        ascending_num = int(ascending_num)

        descending_num = ""
        for num in descending:
            descending_num += str(num)
        descending_num = int(descending_num)

        # update the current number
        current_num = descending_num - ascending_num

        # increase increment counter
        counter += 1
    total += counter
print(f"Kaprekar's routine takes {total} total iterations for all four-digit numbers")