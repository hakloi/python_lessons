# Напишите программу, которая будет на вход принимать дробь и показывать
# первую цифру дробной части числа

import os
clear = lambda: os.system('cls')
clear()

a = float(input('a = '))
result = a*10%10
b = int(result)
print('Остаток от числа {} -> {}'.format(a,b))