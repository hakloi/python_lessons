def view(data):
    if len(data) > 0:
        for item in data:
            print(f'Имя - {item[0]}\nФамилия - {item[1]}\nНомер - {item[2]}\nПримечание - {item[3]}\n')
        else:
            print('Справочник пуст.')

def search_inf(word, data):
    if len(data) > 0:
        for item in data:
            if word in item:
                return item
    else:
        return None
