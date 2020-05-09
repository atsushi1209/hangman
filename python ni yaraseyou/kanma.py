#-------------------------------------------------------------------------------
# Name:        カンマ付け
# Purpose:
#
# Author:      atsushi
#
# Created:     09/05/2020
# Copyright:   (c) atsushi 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def kanma_tsuke(args):
    message = ""
    for i in range(len(args)):
        if i == 0:
            if i == len(args)-1:
                message = args[i] + " only..."
                break
            message = args[i] + ","
        elif i == len(args)-1:
            message = message + " and " + args[i]
        elif i > 0:
            message = message + " " + args[i] + ","

    print(message)


#message = ["apple", "orange", "banana", "peach"]
#message = ["apple", "orange", "banana", "peach", "melon"]
#message = ["apple", "orange"]
message = ["apple"]

kanma_tsuke(message)

