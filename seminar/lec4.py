# Словарь - неупорядоченные коллекции произвольных объектов с доступом по ключу
import os
def clear(): return os.system('cls')
clear()

dictionary = {}
dictionary = \
    {
        'female - 12': '♀',
        'melody - 13': '♪',
        'sun - 15': '☼',
        'man - 11': '♂'
    }

for k in dictionary.values(): # значения
    print(k)

for k in dictionary.keys(): # ключи
    print(k)