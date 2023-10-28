# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Long Vo
#               Bradley Sun
#               Liam Searing
#
# Section:      519
# Assignment:   Go Moves Unit 7 Team Lab
# Date:         10/2/23

#Makes points
turn = 0
valid = True
#Makes and prints an empty board
Board = [[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
for i in range (9):
    for j in range (9):
        print(Board[i][j], end = " ")
    print()
#runs a while loop for the turn counts
while turn < 81:
    print(f"Player 1 '*'")
    #Takes in inputs until a valid input is submitted
    while (valid):
        col = int(input("Please enter the column you want to place your piece on (1-9): "))
        row = int(input("Please enter the column you want to place your piece on (1-9): "))
        col -= 1
        row -= 1
        #If they match or is out of bounds, print unavailable and make them try another input
        if ((row or col) > 8 or (col or row) < 0):
            print("Row or column is out of bounds, try again")
        elif(Board[col][row] == '*' or Board[col][row] == 'o'):
            print("Spot unavailable")
        else:
            #Sets position to player 1 piece and changes valid
            Board[col][row] = '*'
            valid = False
    #Resets valid and adds 1 to turn
    valid = True
    turn += 1
    #Prints board again
    for i in range (9):
        for j in range (9):
            print(Board[i][j], end = " ")
        print()
    #checks if wants to continue playing
    stop = input("Do you want to continue (y/n)")
    #if not, then exit program
    if (stop == "n"):
        exit()
    #Overall logic is repeated for player 2
    print(f"Player 2 'o'")
    while (valid):
        col = int(input("Please enter the column you want to place your piece on (1-9): "))
        row = int(input("Please enter the column you want to place your piece on (1-9): "))
        col -= 1
        row -= 1
        if ((row or col) > 8 or (col or row) < 0):
            print("Row or column is out of bounds, try again")
        elif (Board[col][row] == '*' or Board[col][row] == 'o'):
            print("Spot unavailable")
        else:
            Board[col][row] = 'o'
            valid = False
    valid = True
    turn += 1
    for i in range(9):
        for j in range(9):
            print(Board[i][j], end=" ")
        print()
    stop = input("Do you want to continue (y/n)")
    if (stop == "n"):
        exit()