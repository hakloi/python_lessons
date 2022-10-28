import os
clear = lambda: os.system('cls')
clear()

square = lambda x: x**2

list = [1, 2, 3, 5, 8, 15, 23, 38]

new_list = [(i, square(i)) for i in list if i%2 ==0]

print('Список:')
print(list)

print('\nНовый список:')
print(new_list)