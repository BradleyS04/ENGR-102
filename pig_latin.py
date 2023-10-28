# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Bradley
# Section: ENGR-102-519
# Assignment: 7.25 LAB: Pig latin
# Date: 10/2/23

sentence = str(input("Enter word(s) to convert to Pig Latin: "))
sentenceList = sentence.split()
output = ""
for i in sentenceList:
    word = list(i)
    if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u' or word[0] == 'y':
        output += " "
        for j in word:
            output += j
        output += "yay"
    else:
        #This is for consonants
        output += " "
        if word[1] == 'h' or word[1] == 'r' or word[1] == 'l':
            for j in word[2:]:
                output += j
            output += word[0]
            output += word[1]
            output += "ay"
        else:
            for j in word[1:]:
                output += j
            output += word[0]
            output += "ay"

print(f"In Pig Latin, \"{sentence}\" is: {output}")