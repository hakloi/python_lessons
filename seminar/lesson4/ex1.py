from operator import index
import os
clear = lambda: os.system('cls')
clear()

alphabet_RUS = \
    [
        'а','б','в','г','д','е','ё', 'ж', 'з', 'и',
        'к','л','м','н', 'о', 'п','р','с','т', 'у',
        'ф','х','ц','ч', 'ш', 'щ','ъ','ы','ь', 'э',
        'ю','я', ' '
    ]

alphabet_ENG = \
    [
        'a','b','v','g','d','e','ye','zh','z', 'i',
        'k','l','m','n', 'o', 'p','r','s','t', 'u',
        'f','kh','ts','ch', 'sh', 'shch','','y','','e',
        'yu','ya', ' '
    ]

word = input("Введите слово:\n")
# word_list = list(word.strip()) #strip() - убирает пробелы, list - преобразует всю строку в символы
trans_word = []

print('\nСлово на английском:')
for i in range(len(word)):
    trans_word.append(alphabet_RUS.index(word[i]))
    index = trans_word[i]
    print(alphabet_ENG[index], end='')