colors = ['red', 'green', 'blue']
data = open('demo.txt', 'a')
data.writelines(colors) #разделителей не будет
data.close() # разрываем связь, это обязательно
exit()

path = 'demo.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()