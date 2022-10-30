# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

import os
from unittest import result
clear = lambda: os.system('cls')
clear()

number = int(input('Введите номер четверти: '))
right_number = range(1,5)

if number in right_number:
    print('Данные введены верно!')
else:
    print('Данные введены неверно!')
    exit()

if number == 1:
    print('x > 0 \ny > 0')
elif number == 2:
    print('x < 0 \ny > 0')
elif number == 3:
    print('x < 0 \ny < 0')
else:
    print('x > 0 \ny < 0')