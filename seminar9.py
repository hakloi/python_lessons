import os
clear = lambda: os.system('cls')
clear()

text = input("Введите текст: ")
sum = len(text) * 60
rub = round((sum / 100))
cop = sum % 100
print('{} р. {} коп.'.format(rub, cop))