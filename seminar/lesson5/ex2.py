import os
clear = lambda: os.system('cls')
clear()

triagle = lambda a, b, c: print('Это треугольник!') if a+b>c and c+b>a and a+c>b else print('Это не треугольник!')
triagle(1,1,2)
triagle(7,6,10)