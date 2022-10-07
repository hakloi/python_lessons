# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

import os
clear = lambda: os.system('cls')
clear()

a = int(input('Введите день недели: '))
numbers = range(1,6)
weekend = range(6,8)

if a in numbers:
    print('День {} является будним днем.'.format(a))
elif a in weekend:
     print('День {} является выходным днем.'.format(a))
else:
    print('Введено неверное число - {}. Необходимо число от 1 до 7!'.format(a))