import numpy as np
import matplotlib as ml
import random

mas = [0]*5
for x in range(5):
    mas[x] = [0]*5

list = []
count = 0
for elem in range(20):
    list.append(random.randint(0,10000))

result = [list[:5], list[5:10], list[10:15], list[15:20]]

print(mas)
print(result)



