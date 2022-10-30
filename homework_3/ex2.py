# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import os
clear = lambda: os.system('cls')
clear()

l1 = list(map(int, input('Введите числа через пробел: ').split()))

def multiply_indexes(l1):
    l = len(l1) // 2 + 1 if len(l1) % 2 != 0 else len(l1) // 2
    l2 = [l1[i]*l1[len(l1)-i-1] for i in range (l)]
    print(f'Новый список: {l2}')

multiply_indexes(l1)