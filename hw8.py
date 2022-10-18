# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
import os
clear = lambda: os.system('cls')
clear()

num = int(input('n = '))
l = []
element = 1
print('\nДля n = {}:'.format(num))
for i in range(1,num+1):
    element = element + 3
    l.append(element)
print(l)
print('Сумма чисел списка: ', end='')
print(sum(l))
