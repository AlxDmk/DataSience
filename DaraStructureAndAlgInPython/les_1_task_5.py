# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
num = int(input('Введите порядковый номер буквы: '))
if 0 < num < 36:
    letter = chr(96 + num)
    print(f'Буква: {letter}')
else:
    print('Некорректные данные')
