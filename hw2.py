# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


import os
from unittest import result
clear = lambda: os.system('cls')
clear()

print('Для проверки истинности утверждения \n¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z \nвводите 0 или 1!\n')
x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))
right_numbers = range(0,2)

# Проверка правильности введенных данных
if x in right_numbers and y in right_numbers and z in right_numbers:
    print('Данные введены верно!')
else:
    print('Данные введены неверно!')
    exit()

# Утверждение X ⋁ Y
if x == 0 and y == 0:
    x_v_y = 0
elif x == 1 and y == 1:
    x_v_y = 1
else:
    x_v_y = 0

# Утверждение X ⋁ Y ⋁ Z
if x_v_y == 0 and z == 0:
    x_v_y_v_z = 0
elif x_v_y == 1 and z == 1:
    x_v_y_v_z = 1
else:
    x_v_y_v_z = 0 

# Утверждение ¬(X ⋁ Y ⋁ Z)
if x_v_y_v_z == 0:
    result_1 = 1
    print('\nРезультат утверждения ¬(X ⋁ Y ⋁ Z): {}'.format(result_1))
else:
    result_1 = 0
    print('\nРезультат утверждения ¬(X ⋁ Y ⋁ Z): {}'.format(result_1))


# Утверждение ¬X
if x == 0:
    negative_x = 1
else:
    negative_x = 0

# Утверждение ¬Y 
if y == 0:
    negative_y = 1
else:
    negative_y = 0

# Утверждение ¬Z
if z == 0:
    negative_z = 1
else:
    negative_z = 0

# ¬X ⋀ ¬Y (мы будем использовать символ w вместо )
if negative_x == 0 and negative_y == 0:
    x_w_y = 0
else:
    x_w_y = 1

# Утверждение ¬X ⋀ ¬Y ⋀ ¬Z
if x_w_y == 0 and negative_z == 0:
    result_2 = 0
    print('\nРезультат утверждения ¬X ⋀ ¬Y ⋀ ¬Z: {}'.format(result_2))
else:
    result_2 = 1
    print('\nРезультат утверждения ¬X ⋀ ¬Y ⋀ ¬Z: {}'.format(result_2))

# ПРОВЕРКА!!!!!
if result_1 == result_2:
    print('\nУтверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z ИСТИННО для всех значений предикат!')
    print('Результат ¬(X ⋁ Y ⋁ Z) -> {}\nРезультат ¬X ⋀ ¬Y ⋀ ¬Z -> {}'.format(result_1,result_2))
else: 
    print('Что-то пошло не так...')