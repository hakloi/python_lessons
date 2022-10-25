import os
clear = lambda: os.system('cls')
clear()

a = input('Напишите строку: ')
b = input('Какие повторения вы хотите проверить: ')

print(a.count(b)) 
# считает ПОВТОРЕНИЯ второй строки в первой строке