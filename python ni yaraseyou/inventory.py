#-------------------------------------------------------------------------------
# Name:        inventory
# Purpose:
#
# Author:      atsushi
#
# Created:     10/05/2020
# Copyright:   (c) atsushi 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def display_inventory(inventory):
    print("持ち物リスト：")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + " " + k)
        item_total =item_total + v
    print("アイテム総数：　" + str(item_total))

def add_to_inventory(inventory, added_items):

    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] = inventory[item] + 1



stuff = {"ロープ": 1, "たいまつ": 6, "金貨": 42, "手裏剣": 1, "矢": 12}

dragon_loot = ["金貨","手裏剣","金貨","ルビー","ドラゴンキラー"]

display_inventory(stuff)

add_to_inventory(stuff, dragon_loot)

display_inventory(stuff)
