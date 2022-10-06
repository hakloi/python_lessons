# Напишите программу, которая будет на вход принимать число N
# и выводить числа от -N до N

import os
clear = lambda: os.system('cls')
clear()

a=int(input('a = '))
b = -a
numbers = list(range(-a, a+1))
print('Множество числе от {} до {} -> {}'.format(b, a, numbers))