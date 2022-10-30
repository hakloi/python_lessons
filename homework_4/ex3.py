# Задайте последовательность чисел.
# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
import os
clear = lambda: os.system('cls')
clear()

l1 = list(map(int, input('Введите числа через пробел: ').split()))
print(f'Список: {l1}')

# 1 способ:
# l2 = list(set(l1))
# print(f'Отсортированный список: {l2}')

# 2 способ (dict -> (setdefault) -> list comprehension)
temp = {}
new_l1 = [temp.setdefault(x, x) for x in l1 if x not in temp]
print(f'Отсортированный список: {new_l1}')

