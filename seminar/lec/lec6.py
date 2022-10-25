# Операции с множествами

import os
def clear(): return os.system('cls')
clear()

a = {1, 2, 3, 4, 5}
b = {5, 74, 21, 37, 1}
c = a.copy()
print(c)

u = a.union(b)
print(u)

i = a.intersection(b)
print(i)

dl = a.difference(b)
print(dl)

dr = b.difference(a)
print(dr)