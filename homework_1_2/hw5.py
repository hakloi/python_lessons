# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import os
from unittest import result
clear = lambda: os.system('cls')
clear()
import math

print('Введите координаты первой точки:')
x1 = int(input('x1 = '))
y1 = int(input('y1 = '))

print('Введите координаты второй точки:')
x2 = int(input('x2 = '))
y2 = int(input('y2 = '))

if y1 > y2:
    diff_y = y1 - y2
else:
    diff_y = y2 - y1

if x1 > x2:
    diff_x = x1 - x2
else:
    diff_x = x2 - x1

lenght_between_points = (diff_x**2) + (diff_y**2)
result = math.sqrt(lenght_between_points)
print('\nДлина между точками ({};{}) и ({};{}) равна = {}\n'.format(x1,y1,x2, y2,result))