#-------------------------------------------------------------------------------
# Name:        pprint_sample
# Purpose:
#
# Author:      atsushi
#
# Created:     10/05/2020
# Copyright:   (c) atsushi 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pprint

message = "It was a bright cold day in April, and the clocks were striking thirteen."

count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

#print(count)
#pprint.pprint(count)
print(pprint.pformat(count))
