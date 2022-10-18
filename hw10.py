# Реализуйте алгоритм перемешивания списка

import random
import os
clear = lambda: os.system('cls')
clear()

n = int(input('n = '))
l = []
for i in range(n):
    l.append(random.randint(0,100))
print(l) 

random.shuffle(l)
print('\nПеремешанный список:')
print(l)