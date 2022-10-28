# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

import os
clear = lambda: os.system('cls')
clear()


text = input('Напишите любое предложение:\n')
text_find = 'абв'

lst = [i for i in text.split() if text_find not in i]
print(f'\nРезультат:\n{" ".join(lst)}')
