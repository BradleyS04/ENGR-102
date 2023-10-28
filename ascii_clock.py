# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Long Vo
#               Bradley Sun
#               Liam Searing
#
# Section:      519
# Assignment:   Lab 8.10.1
# Date:         16/10/2023
#


# user inputs time
time = input("Enter the time: ")

# split time into hour and minute
time_split = time.split(":")

# user selects the hour format
clock_type = int(input("Choose the clock type (12 or 24): "))

meridiem = ""

# sets up the meridiem if user chooses 12 hour format
if (clock_type == 12):
    format = True
    if (int(time_split[0]) >= 12):
        meridiem = "PM"
    else:
        meridiem = "AM"
elif (clock_type == 24):
    format = False

# sets up the hour if right condition
if (format == True):
    if (int(time_split[0]) > 12):
        time_split[0] = f"{int(time_split[0]) - 12}"
    elif (int(time_split[0]) == 0):
        time_split[0] = "12"
if (format == False):
    if (int(time_split[0]) == 24):
        time_split[0] = "0"

# tens place of hour
hour1 = int(time_split[0]) // 10

# ones place of hour
hour2 = int(time_split[0]) % 10

# tens place of minute
minute1 = int(time_split[1]) // 10

# ones place of minute
minute2 = int(time_split[1]) % 10

# combines into one list
time_list = [hour1, hour2, minute1, minute2]

# sets up the correct position for colons
if time_list[0] == 0:
    time_list.pop(0)
    limit = 0
else:
    limit = 1

# asks user for their preferred character
char = input("Enter your preferred character: ").lower()

# checks if user's character is acceptable
accept = False
while (accept != True):
    acceptable_char = ["abcdeghkmnopqrsuvwxyz@$&*= "]

    for s in acceptable_char:
        if char in s.lower():
            accept = True
            char.upper()
        else:
            char = input("Character not permitted! Try again: ")

# print blank bline
print()

# sets up 5 row variables
row1 = ""
row2 = ""
row3 = ""
row4 = ""
row5 = ""

# prints correct format for time depending on condition
for i in range(len(time_list)):
    # prints 0
    if (time_list[i] == 0):
        if (char == ""):
            row1 += f"{0}{0}{0} "
            row2 += f"{0} {0} "
            row3 += f"{0} {0} "
            row4 += f"{0} {0} "
            row5 += f"{0}{0}{0} "
        else:
            row1 += f"{char}{char}{char} "
            row2 += f"{char} {char} "
            row3 += f"{char} {char} "
            row4 += f"{char} {char} "
            row5 += f"{char}{char}{char} "
    # prints 1
    elif (time_list[i] == 1):
        if (char == ""):
            row1 += f" {1}  "
            row2 += f"{1}{1}  "
            row3 += f" {1}  "
            row4 += f" {1}  "
            row5 += f"{1}{1}{1} "
        else:
            row1 += f" {char}  "
            row2 += f"{char}{char}  "
            row3 += f" {char}  "
            row4 += f" {char}  "
            row5 += f"{char}{char}{char} "
    # prints 2
    elif (time_list[i] == 2):
        if (char == ""):
            row1 += f"{2}{2}{2} "
            row2 += f"  {2} "
            row3 += f"{2}{2}{2} "
            row4 += f"{2}   "
            row5 += f"{2}{2}{2} "
        else:
            row1 += f"{char}{char}{char} "
            row2 += f"  {char} "
            row3 += f"{char}{char}{char} "
            row4 += f"{char}   "
            row5 += f"{char}{char}{char} "
    # prints 3
    elif (time_list[i] == 3):
        if (char == ""):
            row1 += f"{3}{3}{3} "
            row2 += f"  {3} "
            row3 += f"{3}{3}{3} "
            row4 += f"  {3} "
            row5 += f"{3}{3}{3} "
        else:
            row1 += f"{char}{char}{char} "
            row2 += f"  {char} "
            row3 += f"{char}{char}{char} "
            row4 += f"  {char} "
            row5 += f"{char}{char}{char} "
    # prints 4
    elif (time_list[i] == 4):
        if (char == ""):
            row1 += f"{4} {4} "
            row2 += f"{4} {4} "
            row3 += f"{4}{4}{4} "
            row4 += f"  {4} "
            row5 += f"  {4} "
        else:
            row1 += f"{char} {char} "
            row2 += f"{char} {char} "
            row3 += f"{char}{char}{char} "
            row4 += f"  {char} "
            row5 += f"  {char} "
    # prints 5
    elif (time_list[i] == 5):
        if (char == ""):
            row1 += f"{5}{5}{5} "
            row2 += f"{5}   "
            row3 += f"{5}{5}{5} "
            row4 += f"  {5} "
            row5 += f"{5}{5}{5} "
        else:
            row1 += f"{char}{char}{char} "
            row2 += f"{char}   "
            row3 += f"{char}{char}{char} "
            row4 += f"  {char} "
            row5 += f"{char}{char}{char} "
    # prints 6
    elif (time_list[i] == 6):
        if (char == ""):
            row1 += f"{6}{6}{6} "
            row2 += f"{6}   "
            row3 += f"{6}{6}{6} "
            row4 += f"{6} {6} "
            row5 += f"{6}{6}{6} "
        else:
            row1 += f"{char}{char}{char} "
            row2 += f"{char}   "
            row3 += f"{char}{char}{char} "
            row4 += f"{char} {char} "
            row5 += f"{char}{char}{char} "
    # prints 7
    elif (time_list[i] == 7):
        if (char == ""):
            row1 += f"{7}{7}{7} "
            row2 += f"  {7} "
            row3 += f"  {7} "
            row4 += f"  {7} "
            row5 += f"  {7} "
        else:
            row1 += f"{char}{char}{char} "
            row2 += f"  {char} "
            row3 += f"  {char} "
            row4 += f"  {char} "
            row5 += f"  {char} "
    # prints 8
    elif (time_list[i] == 8):
        if (char == ""):
            row1 += f"{8}{8}{8} "
            row2 += f"{8} {8} "
            row3 += f"{8}{8}{8} "
            row4 += f"{8} {8} "
            row5 += f"{8}{8}{8} "
        else:
            row1 += f"{char}{char}{char} "
            row2 += f"{char} {char} "
            row3 += f"{char}{char}{char} "
            row4 += f"{char} {char} "
            row5 += f"{char}{char}{char} "
    # prints 9
    else:
        if (char == ""):
            row1 += f"{9}{9}{9} "
            row2 += f"{9} {9} "
            row3 += f"{9}{9}{9} "
            row4 += f"  {9} "
            row5 += f"{9}{9}{9} "
        else:
            row1 += f"{char}{char}{char} "
            row2 += f"{char} {char} "
            row3 += f"{char}{char}{char} "
            row4 += f"  {char} "
            row5 += f"  {char} "

    if (i == limit):
        row1 += "  "
        row2 += ": "
        row3 += "  "
        row4 += ": "
        row5 += "  "

# prints its respective meridiem
if (meridiem == "AM"):
    row1 += f" A  M   M"
    row2 += f"A A MM MM"
    row3 += f"AAA M M M"
    row4 += f"A A M   M"
    row5 += f"A A M   M"
elif (meridiem == "PM"):
    row1 += f"PPP M   M"
    row2 += f"P P MM MM"
    row3 += f"PPP M M M"
    row4 += f"P   M   M"
    row5 += f"P   M   M"

# prints the clock
print(row1.rstrip())
print(row2.rstrip())
print(row3.rstrip())
print(row4.rstrip())
print(row5.rstrip())