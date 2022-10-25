import os
def clear(): return os.system('cls')
clear()

# кортеж - неизменяемый список

a, b = 3, 4 #множественное присваивание
l = (3, 4)
print(l)
print(l[-1])

# присваивание на кортежах не работает

print('\nКортеж по строкам через цикл for:')
for item in l:
    print(item)