import datetime

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


def show_notes(notebook, error_message: str):
    if not notebook:
        show_red_message(error_message)
        return False
    else:
        print(f'\033[34m{notebook}\033[0m')
        return True


def add_note(n_id: int):
    n_id = n_id
    header = input("Введите название заметки: ")
    content = input("Введите тело заметки: ")
    dt = datetime.datetime.today()
    # print(dt.year)
    # print(dt.month)
    # print(dt.day)
    # print(dt.hour)
    # print(dt.minute)
    return [n_id, header, content, dt.strftime("%d/%m/%Y %H:%M")]


def change_note(n_id: int):
    show_yellow_message("Введите новые данные, или оставьте поле пустым, если нет изменений")
    note = add_note(n_id)
    return note


def input_choice(message: str):
    show_yellow_message(message)
    return input().lower()


def input_index(message: str):
    index = input(message)
    if index.isdigit():
        return int(index)


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
