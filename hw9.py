# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

import os
clear = lambda: os.system('cls')
clear()

from random import Random, randint

num = int(input('num = '))
l = []
for i in range(num):
    l.append(randint(-num,num+1))
print(l)

x = open('file.txt','r')
result = l[int(x.readline())] * l[int(x.readline(2))]
print(result)