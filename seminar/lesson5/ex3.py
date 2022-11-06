import os
clear = lambda: os.system('cls')
clear()

a = [4, 3, -10, 1, 7, 12]
# b = [i for i in a if i%2==0]
# c = [i for i in a if i%2!=0]
# print(f'Первоначальный список: {a}')
# print(f'Новый список b+c: {b+c}')
a.sort(key=lambda x: x%2)
print(a)