#-------------------------------------------------------------------------------
# Name:        三目並べ
# Purpose:
#
# Author:      atsushi
#
# Created:     10/05/2020
# Copyright:   (c) atsushi 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

the_board = {"top-L": " ", "top-M": " ", "top-R": " ",
             "mid-L": " ", "mid-M": " ", "mid-R": " ",
             "low-L": " ", "low-M": " ", "low-R": " ",}





def print_board(board):
    print(board["top-L"] + "|" + board["top-M"] + "|" + board["top-R"])
    print("-+-+-")
    print(board["mid-L"] + "|" + board["mid-M"] + "|" + board["mid-R"])
    print("-+-+-")
    print(board["low-L"] + "|" + board["low-M"] + "|" + board["low-R"])


turn = "X"
for i in range(9):
    print_board(the_board)
    print(turn + "の番です。どこに打つ？")
    move = input()
    the_board[move] = turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X"


