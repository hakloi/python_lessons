import os
def clear(): return os.system('cls')
clear()

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

list = []
for e in range(1, 21):
    list.append(fib(e))
print(list)