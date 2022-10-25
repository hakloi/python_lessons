#with open('demo.txt', 'w') as data:
#   data.write('\nLINE 2\n')
#   data.write('LINE 3\n')  

colors = ['red', 'green', 'blue3']
data = open('demo.txt', 'w')
data.writelines(colors) #разделителей не будет
data.write('\nLINE 2\n')
data.write('LINE 3\n')
data.close() # разрываем связь, это обязательно

path = 'demo.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()
exit()