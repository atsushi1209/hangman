#list = [["cat", "dog", "mouse"],["orange", "apple", "lemon"]]
list = [["ねこ", "犬", "ねずみ"],["みかん", "林檎", "檸檬"]]


import csv

with open("charenge9-4.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter=",")
#    writer.writerow(list[0])
#    writer.writerow(list[1])
    for output in list:
        writer.writerow(output)
     
