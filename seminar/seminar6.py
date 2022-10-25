import os
clear = lambda: os.system('cls')
clear()

n = int(input("n = "))

element = -3
for i in range(0, n):
    print(element**i, end=" ")