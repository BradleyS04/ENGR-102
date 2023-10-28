# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Bradley
# Section: ENGR-102-519
# Assignment: 7.26.1: LAB: Leet speak
# Date: 10/2/23

text = str(input("Enter some text: "))
textList = text.split()
output = ""
executed = False
leet = {'a': '4', 'e': '3', 'o': '0', 's': '5', 't': '7'}
for i in textList:
    word = list(i)
    counter = 0
    while(counter < len(word)):
        #Iterates through the dictionary to find a matching pair
        for j in leet:
            if word[counter] == j:
                output += leet[j]
                executed = True
                break
        if (not executed):
            output += word[counter]
        executed = False
        counter += 1
    output += " "
print(f"In leet speak, \"{text}\" is: ")
print(output)
