#Sudoku Solver 12/11/19

import time
from random import shuffle as shuffle
from random import randint as randint

board = [
    [0,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,0,0,4,0,2,6,0],
    [0,0,0,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,0,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


#Prints the board to the screen and adds dividers
def print_board(b):
    """Reads in a board and then prints it to the console"""
    for col in range(len(b)):
        if col % 3 == 0 and col != 0:
            print("- - - - - - - - - - - -")
        for row in range(len(b[col])):
            if row % 3 == 0 and row != 0:
                print(" | ", end="")
            print(str(b[col][row]) + " ", end="")
        print()

#Finds an empty spot if there is one (starts with first row)
def empty_spot(b):
    """Reads in a board and then returns a position of an empty spot (row, col)"""
    for row in range(len(b)):
        for col in range(len(b)):
            if b[row][col] == 0:
                return row, col
    return False

#Determines if the test number and position are valid
def valid(b, num, pos):
    """Reads in the board, a test number to plug in, and the position 
and then returns if that is a valid number"""  
    #Checks row
    for row in range(len(b[0])):
        if b[pos[0]][row] == num and pos[1] != row:
            return False

    #Checks Column
    for col in range(len(b)):
        if b[col][pos[1]] == num and pos[0] != col:
            return False
    
    #Checks 3x3 box
    box_row = pos[0] // 3
    box_col = pos[1] // 3
    for col_x in range(box_row * 3, box_row * 3 + 3):
        for row_x in range(box_col * 3, box_col * 3 + 3):
            if b[col_x][row_x] == num and (col_x, row_x) != pos:
                return False
    return True #Returns True if there is no problems

#Defines main function (runs until solved)
def solve(b):
    """Reads in a board and then solves it"""
    spot = empty_spot(b)
    if not spot:
        return True
    else:
        row, col = spot

    #Tries each number 1-9 in the empty spot until one creates no errors
    numlist = [1,2,3,4,5,6,7,8,9]
    shuffle(numlist)
    for test in numlist:
        if valid(b, test, (row, col)):
            b[row][col] = test

            #Uses recursion to go down the path trying that test case
            if solve(b):
                return True
            
            b[row][col] = 0

    #Allows the recursion to go back a step and back track to fix the error
    return False

#Creates main function which calls the other functions in order and prints results
def main():
    print("The unsolved board is:\n")
    print_board(board)
    start = time.time()
    solve(board)
    print("\n-------------------------\n")
    print("The solved board is:\n")
    print_board(board)
    finish = time.time()
    print("\nThat took", finish - start, "secs")

main()

