list = [["cat", "dog", "mouse"],["orange", "apple", "lemon"]]


import csv

with open("charenge9-3.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter=",")
#    writer.writerow(list[0])
#    writer.writerow(list[1])
    for output in list:
        writer.writerow(output)
     
