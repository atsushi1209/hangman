#-------------------------------------------------------------------------------
# Name:        2次元リスト表示
# Purpose:
#
# Author:      atsushi
#
# Created:     09/05/2020
# Copyright:   (c) atsushi 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def hyouzi(args):
    out_grid = ""
    row = len(args)
    for i in range(row):
        current_row = args[i]
        for j in range(len(current_row)):
            if j != len(current_row)-1:
                print(args[i][j], end="")
            else:
                print(args[i][j])



grid = [[".",".","0","0",".","0","0",".","."],
        [".","0","0","0","0","0","0","0","."],
        [".","0","0","0","0","0","0","0","."],
        [".",".","0","0","0","0","0",".","."],
        [".",".",".","0","0","0",".",".","."],
        [".",".",".",".","0",".",".",".","."],
        ]

hyouzi(grid)