# Напишите программу, которая будет преобразовывать
# десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
import os
clear = lambda: os.system('cls')
clear()

num_decimal = int(input('Введите десятичное число: '))
b = ''
while num_decimal > 0:
    b = str(num_decimal % 2) + b
    num_decimal = num_decimal // 2
 
print(f'Двоичное число: {b}')