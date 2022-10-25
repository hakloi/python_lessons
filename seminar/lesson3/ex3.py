import os
clear = lambda: os.system('cls')
clear()

array = ['pdsfoispdofisdpfasm,f5432546']
number = 2
for word in array:
    if str(number) in word:
        print(True)
    else:
        print(False)
