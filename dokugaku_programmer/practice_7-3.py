animal = ["cat", "dog", "mouse", "bird", "monkey"]

n = 0
for output in animal:
    print("No.{}: {}".format(n, animal[n]))
    n = n + 1

for i, output in enumerate(animal):
    print(i)
#    print(animal[i])
    print(output)
    
