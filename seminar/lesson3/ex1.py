
from itertools import count
import os
clear = lambda: os.system('cls')
clear()

count_p = 0
count_o = 0

text = input("Введите произвольную последовательность букв О и Р: ")

for char in text:
    if char == "Р":
        count_p += 1
    elif char == "О":
        count_o += 1
    else:
        print('Неправильно введеные данные')
print('Решка: {}'.format(count_p))
print('Орел: {}'.format(count_o))

if count_p == 0:
    print('\nРешек нет...')