# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import os
clear = lambda: os.system('cls')
clear()

n = int(input('n = '))
element = 1
print("пусть N = {}".format(n))
print("[", end='')
for i in range(1,n):
    element = i*element
    print(element, end=" ")
print("]")