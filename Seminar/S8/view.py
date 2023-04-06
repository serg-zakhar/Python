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
            print("Неверный пункт меню")


def show_contacts(book: list[dict], error_message: str):
    if not book:
        show_red_message(error_message)
        return False
    else:
        for i, contact in enumerate(book, 1):
            print(f'\033[34m {i}. {contact.get("name"):<20} '
                  f'{contact.get("phone"):<20} '
                  f'{contact.get("comment"):<20}\033[0m')
        return True


def add_contact() -> dict:
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    comment = input("Введите комментарий:  ")
    return {'name': name, 'phone': phone, 'comment': comment}


def input_index(message: str):
    index = input(message)
    if index.isdigit():
        return int(index)


def input_search(message: str):
    return input(message)


def change_contact(book: list[dict], index: int):
    show_yellow_message("Введите новые данные, или оставьте поле пустым, если нет изменений")
    contact = add_contact()
    show_blue_message(f"Контакт {index - 1} изменен")
    return {'name': contact.get('name') if contact.get('name') else book[index - 1].get('name'),
            'phone': contact.get('phone') if contact.get('phone') else book[index - 1].get('phone'),
            'comment': contact.get('comment') if contact.get('comment') else book[index - 1].get('comment')}


def show_red_message(message: str):
    print(f'\033[31m {"-" * len(message)}')
    print(message)
    print(f'{"-" * len(message)}\033[0m')


def show_yellow_message(message: str):
    print(f'\033[33m {"-" * len(message)}')
    print(message)
    print(f'{"-" * len(message)}\033[0m')


def show_blue_message(message: str):
    print(f'\033[34m {"-" * len(message)}')
    print(message)
    print(f'{"-" * len(message)}\033[0m')
