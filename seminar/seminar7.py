import os
clear = lambda: os.system('cls')
clear()

n = int(input("n = "))
first = 1
second = 1
for i in range(1,n+1):
    first = 3 * i + 1
    second = 3 * i - 1
    print('{}, {}; '.format(first, second), end=" ")