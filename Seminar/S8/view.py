# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

import text_fields


def main_menu() -> int:
    print(text_fields.main_menu)
    length_menu = len(text_fields.main_menu.split('\n')) - 1
    while True:
        num_menu = (input("Выберите пункт меню: "))
        if num_menu.isdigit() and 0 < int(num_menu) <= length_menu:
            return int(num_menu)
        else:
            show_red_message("Неверный пункт меню")


def show_contacts(book, error_message: str):
    if not book:
        show_red_message(error_message)
        return False
    else:
        print(f'\033[34m{book}\033[0m')
        return True


def add_contact():
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    comment = input("Введите комментарий:  ")
    # return {'name': name, 'phone': phone, 'comment': comment}
    return [name, phone, comment]


def input_index(message: str):
    index = input(message)
    if index.isdigit():
        return int(index)


def input_search(message: str):
    return input(message)


def input_choice(message: str):
    show_yellow_message(message)
    return input().lower()


def change_contact(book):
    show_yellow_message("Введите новые данные, или оставьте поле пустым, если нет изменений")
    contact = add_contact()
    return contact


def show_red_message(message: str):
    print(f'\033[31m{"-" * len(message)}')
    print(message)
    print(f'{"-" * len(message)}\033[0m')


def show_yellow_message(message: str):
    print(f'\033[33m{"-" * len(message)}')
    print(message)
    print(f'{"-" * len(message)}\033[0m')


def show_blue_message(message: str):
    print(f'\033[34m{"-" * len(message)}')
    print(message)
    print(f'{"-" * len(message)}\033[0m')
