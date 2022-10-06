# a=[1,2,3]
# b=a[:]
# print(b)

#print(10,11,12, sep="__") #по умолчанию с пробелами, sep - разделитель

#Задание 1: Напишите программу, которая принимает на вход два числа и проверяет,
# является ли одно число квадратом другого.

import os
clear = lambda: os.system('cls')
clear()

a=int(input('a = '))
b=int(input('b = '))

if a**2 == b:
    print('-> да')
elif b**2 == a:
    print('-> да')
else:
    print('-> нет')
