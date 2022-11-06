import os
clear = lambda: os.system('cls')
clear()

text = list(map(str, input('Введите строку: ').strip()))
zipper = [i for i in range(11)]
result = list(zip(text, zipper))
print(*result)