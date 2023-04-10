import view
import model
import phonebook

pb_opened = False


def start():
    while True:
        # pb = model.get_phonebook()
        pb = phonebook.PhoneBook('phonebook.txt')
        num_menu = view.main_menu()
        match num_menu:
            case 1:
                if pb_opened:
                    view.show_red_message("Телефонная книга уже открыта")
                else:
                    pb.open()

                    # model.open_phonebook()
                    # view.show_blue_message("Телефонная книга открыта")
            case 2:
                if view.show_contacts(pb, "Телефонная книга пуста или не открыта"):
                    if input(f'\033[33m {"Записать телефонную книгу? [y/n]: "}\033[0m').lower() == 'y':
                        model.save_phonebook()
                        view.show_blue_message("Телефонная книга успешно сохранена")
                    else:
                        view.show_yellow_message("Телефонная книга не сохранена")
            case 3:
                view.show_contacts(pb, "Телефонная книга пуста или не открыта")
            case 4:
                if view.show_contacts(pb, "Телефонная книга пуста или не открыта"):
                    search = view.input_search("Введите строку для поиска: ")
                    result = model.find_contact(search)
                    view.show_contacts(result, "Контакты не найдены")
            case 5:
                if not pb_opened:
                    view.show_red_message("Телефонная книга не открыта")
                else:
                    view.show_contacts(pb, "Телефонная книга пуста")
                    view.show_yellow_message("Добавление нового контакта: ")
                    model.add_contact(view.add_contact())
                    view.show_blue_message("Контакт успешно добавлен")
            case 6:
                if view.show_contacts(pb, "Телефонная книга пуста или не открыта"):
                    index = view.input_index("Выберите контакт для изменения: ")
                    if index and 0 < index <= len(pb):
                        contact = view.change_contact(pb, index)
                        model.change_contact(contact, index)
                    else:
                        view.show_red_message("Выбранный контакт не найден")
            case 7:
                if view.show_contacts(pb, "Телефонная книга пуста или не открыта"):
                    index = view.input_index("Выберите контакт для удаления: ")
                    if index and 0 < index <= len(pb):
                        model.delete_contact(index)
                        view.show_blue_message("Контакт успешно удален")
                    else:
                        view.show_red_message("Выбранный контакт не найден")
            case 8:
                if view.show_contacts(model.del_phone_book, "Отсутствуют контакты для восстановления"):
                    index = view.input_index("Выберите контакт для восстановления: ")
                    if index and 0 < index <= len(model.del_phone_book):
                        model.restore_contact(index)
                        view.show_blue_message("Контакт успешно восстановлен")
                    else:
                        view.show_red_message("Выбранный контакт не найден")
            case 9:
                view.show_blue_message("Выход из программы")
                return