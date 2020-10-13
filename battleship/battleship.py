# A simple game of Battleship. 'Nuff said.
# Written in Notepad++, tested with Python 2.7.16 running
# through the Windows command line.

# Santtu "MFG38" Pesonen, 2019-12-28

from random import randint

board = []
for i in range(8):
    board.append(['O'] * 8)

def print_board(board):
    for row in board:
        print " ".join(row)

def random_row(board):
    return randint(0,len(board) - 1)

def random_col(board):
    return randint(0,len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(10):
    print "Turn", turn + 1
    print_board(board)
    
    guess_row = int(raw_input("Guess row: "))
    guess_col = int(raw_input("Guess column: "))
    
    if guess_row == ship_row and guess_col == ship_col:
        print "AAAAAAAAA I'M DROWNING gg you found my ship."
        break
    else:
        if guess_row not in range(0,8) or guess_col not in range(0,8):
            print "ERROR: Guess out of bounds!"
        elif board[guess_row][guess_col] == "X":
            print "ERROR: Nothing already found there!"
        else:
            print "Hah, nope! Not over there!"
            board[guess_row][guess_col] = "X"
        
        if turn == 9:
            print "GAME OVER"

