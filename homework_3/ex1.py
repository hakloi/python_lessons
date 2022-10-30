# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import os
clear = lambda: os.system('cls')
clear()


l1 = list(map(int, input('Введите данные через пробел:\n').split()))
print(f'\nСписок: {l1}')

def sum_odd_index(l1):
    s = 0
    print('Числа на нечетных индексах: ', end='')
    for i in range(len(l1)):
        if i % 2 != 0:
            s += l1[i]
            print(f'{l1[i]} ', end='')
    print(f'\nСумма: {s}')

sum_odd_index(l1)