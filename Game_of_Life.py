#created by TJ 7/21/24
import random
import time
import os
import copy

def random_state(width, height):
    board = [["N"]*(width + 2)]
    for I in range(height):
        row = ["N"]
        for I in range(width):
            value = random.random()
            row.append(round(value))
        row.append("N")
        board.append(row)
    board.append(["N"]*(width + 2))
    return board

def render(state):
    os.system('clear')
    cols = []
    for row in state:
        rowstr = ""
        for cell in row:
            if cell == 0:
                rowstr += ". "
            elif cell == 1:
                rowstr += u"\u2588 "
            else:
                rowstr += "$ "
        cols.append(rowstr)
    print("\n".join(cols) )
    return



def update_cell(board,cell):
    #cell [row, col]
    state = board[cell[0]][cell[1]] 
    if state != 1  and state != 0:
        return "N"
    alive = 0
    if board[cell[0] + 1][ cell[1]] == 1:
        alive += 1
    if board[cell[0] + 1][ cell[1]-1] == 1:
        alive += 1
    if board[cell[0] + 1][ cell[1]+1] == 1:
        alive += 1
    if board[cell[0] - 1 ][cell[1]] == 1:
        alive += 1
    if board[cell[0] - 1 ][cell[1]-1] == 1:
        alive += 1
    if board[cell[0] - 1 ][cell[1]+1] == 1:
        alive += 1
    if board[cell[0]  ][cell[1]-1] == 1:
        alive += 1
    if board[cell[0]  ][cell[1]+1] == 1:
        alive += 1
    #print(str(alive) + str(cell))
    
    if state == 1:
        if alive < 2:
            return 0
        if alive == 2 or alive == 3:
            return 1
        if alive > 2:
            #print("fe")
            return 0
    if state == 0 and alive == 3:
        return 1
    return 0

def update_board(board):
    newboard = copy.deepcopy(board)

    newboard[1][5] = 1

    height = len(board)
    width = len(board[0])
    for row in range(height):
        for col in range(width):
            
            newboard[row][col] = update_cell(board, [row,col])
    return newboard
    




    






board = [
    ["$","$","$","$","$","$","$"],
    ["$",0,0,0,0,0,"$"],
    ["$",0,0,1,1,1,"$"],
    ["$",0,1,1,1,0,"$"],
    ["$",0,0,0,0,0,"$"],
    ["$",0,0,0,0,0,"$"],
    ["$","$","$","$","$","$","$"]
]

board = random_state(400,200)


#render(newboard)
#update_board(board)
#render(update_board(newboard))
#print(update_cell(newboard,[1,5]))

#for I in range(1000):
#    time.sleep(0.001)
#    os.system('clear')
#    render(board)
#    board = update_board(board)



def main():
    print("Game of Life")
    width = int(input("enter width: "))
    height = int(input("enter height: "))
    cycles = int(input("enter how many cycles"))
    board = random_state(width,height)
    count = 0
    while count < cycles:
        render(board)
        board = update_board(board)
        count += 1
        time.sleep(0.1)
    print("Done")

main()