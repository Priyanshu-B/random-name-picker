chosefrom = ["A", "B", "C"]
names = []
for i in range(10):
    for j in chosefrom:
        names.append(j)

import random as rd 
rd.shuffle(names)
print(rd.choice(names))