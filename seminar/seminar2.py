# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

import os
clear = lambda: os.system('cls')
clear()

a=int(input('a = '))
b=int(input('b = '))
c=int(input('c = '))
d=int(input('d = '))

print('Максимальное число:', + max(a,b,c,d))