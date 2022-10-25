# Множества
import os
def clear(): return os.system('cls')
clear()

names = {'Violet', 'Daria', 'Yan'}
print(names)

names.add('Dasha') # 'Daria' не добавится, так как она уже есть
print(names)

names.add('Daria')
print(names)

names.remove('Yan')
print(names)

names.discard('Dasha')
print(names)

#names.clear()
#print(names)

print('\nИ остались только...')
names.add('Maris') 
print(names)