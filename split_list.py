# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Bradley
# Section: ENGR-102-519
# Assignment: 7.27 LAB: Split list
# Date: 10/4/23

sentence = input("Enter numbers: ")
sentenceList = sentence.split()
side1 = []
side2 = []
sum1 = 0
sum2 = 0
intList = []
#Creats a integer list
for i in sentenceList:
    intList.append(int(i))
#This checks the list
for i in range(len(sentenceList)):
    side1 = intList[0:i+1]
    side2 = intList[i+1:]
    for j in side1:
        sum1+=j
    for k in side2:
        sum2+=k
    if sum1 == sum2:
        print(f"Left: {side1}")
        print(f"Right: {side2}")
        print(f"Both sum to {sum1}")
        exit()
    sum1 = 0
    sum2 = 0
print("Cannot split evenly")
