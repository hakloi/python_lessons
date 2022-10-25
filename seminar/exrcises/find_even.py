import os
def clear(): return os.system('cls')
clear()

def f(num):
    if num % 2 == 0:
        print('Number {} -> is envy'.format(num))
    else:
        print('Number {} -> is odd'.format(num))