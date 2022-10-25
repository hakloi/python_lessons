# Напишите программу, которая принимает на вход число и проверяет,
# кратно ли она 5 и 10 или 15, но не 30

import os
clear = lambda: os.system('cls')
clear()

a = int(input('a = '))
if a%5 == 0 and a%10 == 0 and a%15 and a%30 != 0:
    print('{} - число кратно 5, 10 или 15, но не 30!'.format(a))
else:
    print('{} - число не подходит!'.format(a))