#-------------------------------------------------------------------------------
# Name:        collats数列
# Purpose:　3章　演習プロジェクト
#
# Author:      atsushi
#
# Created:     05/05/2020
# Copyright:   (c) atsushi 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def collatz(number):
    hantei = number % 2
    if hantei == 0:
        return int(number / 2)
    elif hantei == 1:
        return int(3 * number + 1)


while True:
    input_data = input("整数を入力してください。：")

    try:
        int(input_data)
        break
    except ValueError:
        print("{}が入力されました。整数を入力してください。".format(input_data))


while True:
    modorichi = collatz(int(input_data))
    if modorichi == 1:
        print(modorichi)
        break
    else:
        print(modorichi)
        input_data = modorichi



