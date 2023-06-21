import view
import phonebook


def start():
    pb = phonebook.PhoneBook("phonebook.txt")
    pb_deleted = []

    while True:
        choice = view.main_menu()
        match choice:
            case 1:  # Показать все контакты
                view.show_contacts(pb, "Телефонная книга пуста")
            case 2:  # Найти контакт
                search = pb.find_contact(view.input_search("Введите строку для поиска: "))
                view.show_contacts(search, "Контакты не найдены")
            case 3:  # Добавить контакт
                pb.new_contact(*view.add_contact())
                view.show_blue_message('Контакт добавлен!')
            case 4:  # Изменить контакт
                view.show_contacts(pb, "Телефонная книга пуста")
                index = view.input_index("Выберите контакт для изменения: ")
                if index and 0 < index <= len(pb.contacts):
                    pb.change_contact(index - 1, *view.change_contact(pb))
                    view.show_blue_message(f"Контакт {index} изменен")
                else:
                    view.show_red_message("Введен некорректный номер контакта")
            case 5:  # Удалить контакт
                view.show_contacts(pb, "Телефонная книга пуста")
                index = view.input_index("Выберите контакт для удаления: ")
                if index and 0 < index <= len(pb.contacts):
                    pb_deleted.append(pb.contacts[index - 1])
                    pb.delete_contact(index - 1)
                    view.show_blue_message('Контакт успешно удален!')
                else:
                    view.show_red_message("Введен некорректный номер контакта")
            case 6:  # Восстановить контакт
                # view.show_contacts(pb_deleted, "Отсутствуют контакты для восстановления")
                if pb_deleted:
                    for i, contact in enumerate(pb_deleted, 1):
                        print(f'\033[34m{i}. {contact}\n\033[0m')
                        index = view.input_index("Выберите контакт для восстановления: ")
                        if index and 0 < index <= len(pb_deleted):
                            del_contact = pb_deleted[index - 1]
                            pb.new_contact(del_contact.name, del_contact.phone, del_contact.comment)
                            pb_deleted.pop(index - 1)
                            view.show_blue_message('Контакт успешно восстановлен!')
                        else:
                            view.show_red_message("Введен некорректный номер контакта")
                else:
                    print(view.show_red_message("Отсутствуют контакты для восстановления"))
            case 7:  # Сохранить изменения
                if view.input_choice("Вы хотите сохранить изменения? (y/n): ") == "y":
                    pb.save()
                    view.show_blue_message("Телефонная книга успешно сохранена")
                else:
                    view.show_red_message("Телефонная книга не сохранена")
            case 8:  # Выход
                if view.input_choice("Вы хотите сохранить изменения перед выходом? (y/n): ") == "y":
                    pb.save()
                    view.show_blue_message("Телефонная книга успешно сохранена")
                    view.show_blue_message("Выход из программы")
                    return
                else:
                    view.show_blue_message("Выход из программы")
                    return
