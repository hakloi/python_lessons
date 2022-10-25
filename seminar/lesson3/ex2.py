import os
clear = lambda: os.system('cls')
clear()

n = \
    ['osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen',
    'anton', 'aoooooooooontooooo', 'elelelelelelelelelel', 'ntoneeee',
    'tonee', '253235235a5323352n25235352t253523523235oo235523523523n',
    'antoooooooooooooooooooooooooooooooooooooooooooooooooooon', 'unton']

count_anton = 0
for i in n:
    if i == 'anton':
        count_anton += 1
    else:
        count_anton += 0
print("Зараженных холодильников: {}!".format(count_anton))
