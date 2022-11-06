from import_data import import_inf
from export_data import export_inf
from user import view, search_inf

# Приветствие
def greet():
    username = input('Введите ваше имя: ')
    print(f'Добро пожаловать в книгу контактов, {username}!')

# Разделитель для записи в файл
def sep_choice():
    sep = input("Введите разделитель: ")
    if sep == "":
        sep = None
    return sep

# Добавить контакт
def input_info():
    name = input('Имя: ')
    surname = input('Фамилия: ')
    valid = False
    while valid == False:
        while not valid:
            try:
                tel = input('Введите номер телефона: ')
                if len(tel) != 11:
                    print('В номере телефона должно быть 11 цифр.')
                else:
                    tel = int(tel)
                    valid = True
            except:
                print('Номер телефона должен состоять только из цифр.')
    note = input('Примечание: ')
    return [name, surname, tel, note]


# Выбор функций
def choices():
    print('Выберите что вы хотите сделать: ')
    num = int(input('1 - посмотреть контакт\n2 - добавить контакт\n3 - экспорт контакта:\n'))
    if num == 1:
        print('Найти контакт>>>')
        word = input('Введите ключевое слово: ')
        date = export_inf()
        item = search_inf(word, date)
        if item != None:
            print(f'Имя - {item[0]}\nФамилия - {item[1]}\nНомер - {item[2]}\nПримечание - {item[3]}')
        else:
            print('Контакта не существует. Проверьте введенные данные.')
    elif num == 2:
        print('Добавить контакт>>>\n')
        sep = sep_choice()
        import_inf(input_info(), sep)
    elif num == 3:
        print('Эскпорт контакта>>>\n')
        data = export_inf()
        view(data)
    else: 
        print('Вы ввели неверные данные!')