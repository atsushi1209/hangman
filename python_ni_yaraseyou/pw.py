#! python3
#-------------------------------------------------------------------------------
# Name:        パスワード管理
# Purpose:
#
# Author:      atsushi
#
# Created:     16/05/2020
# Copyright:   (c) atsushi 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

PASSWORD = {"email" : "abedefg",
            "blog" : "highklm",
            "luggage" : "nopqrst"}


import sys
import pyperclip

if len(sys.argv) < 2:
    print("使い方： python pw.py [アカウント名]")
    print("パスワードをクリップボードにコピーします")
    sys.exit()


account = sys.argv[1] # 最初のコマンドライン引数がアカウント名


if account in PASSWORD:
    pyperclip.copy(PASSWORD[account])
    print(account + "のパスワードをクリップボードにコピーしました")
else:
    print(account + "というアカウント名はありません")


