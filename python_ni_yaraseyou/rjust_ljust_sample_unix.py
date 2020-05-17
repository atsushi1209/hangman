#!/usr/bin/python3
#!/usr/bin/env python3
#-------------------------------------------------------------------------------
# Name:        rjust(),ljust()使い方
# Purpose:
#
# Author:      atsushi
#
# Created:     10/05/2020
# Copyright:   (c) atsushi 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def print_picnic(items_dict, left_width, right_width):
    print("PICNIC ITEMS".center(left_width + right_width, "-"))
    for k, v in items_dict.items():
        print(k.ljust(left_width, ".") + str(v).rjust(right_width))

picnic_items = {"sandwiches": 4, "apples": 12, "cups":4, "cookies":8000}


print_picnic(picnic_items, 12, 5)
print_picnic(picnic_items, 20, 6)


