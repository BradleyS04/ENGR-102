list = [[ 0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5]]
for row in list:
    for col in row:
        print(col, end = "")
    print()
answer = "programming"
Valid = True
while Valid:
    check = input()
    if(check in answer):
        print("correct")
        Valid = False
mystr = "Howdy! Welcome to Texas A&M Engineering!"
print(mystr[:5] + mystr[6] + mystr[18:] + ' students!')
