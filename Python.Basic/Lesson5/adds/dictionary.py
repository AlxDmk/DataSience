dictionary_en_ru = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}


def translate(text):
    return dictionary_en_ru[text] if text in dictionary_en_ru else "Нет перевода этого слова"

