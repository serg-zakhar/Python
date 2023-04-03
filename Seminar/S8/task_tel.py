# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
from unittest import case


# 1. Открыть файл телефонной книги
# 2. Сохранить файл телефонной книги
# 3. Показать все контакты
# 4. Найти контакт
# 5. Добавить контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход

def show_menu() -> int:
    print("1. Открыть файл телефонной книги")
    print("2. Сохранить файл телефонной книги")
    print("3. Показать все контакты")
    print("4. Найти контакт")
    print("5. Добавить контакт")
    print("6. Изменить контакт")
    print("7. Удалить контакт")
    print("8. Выход")
    num = 0
    while num < 1 or num > 8:
        num = int(input("Выберите пункт меню: "))
    return num

# def action_menu(num: int):
#     if num == 1:
#         list_phonebook = open_phonebook(file_name)
#     elif num == 2:


def open_phonebook(file_name):
    with open(file_name, 'r', encoding="UTF-8") as f:
        list_phonebook = f.readlines()
        return list_phonebook


def save_phonebook(file_name, list_phonebook: list):
    with open(file_name, 'w', encoding="UTF-8") as f:
        for line in list_phonebook:
            f.write(line)


file_name = input("Введите имя файла телефонного справочника: ")
list_phonebook = open_phonebook(file_name)
num = show_menu()
if num == 1:
    print(open_phonebook(file_name))
elif num == 2:
    save_phonebook(file_name, list_phonebook)
# action_menu(num)
