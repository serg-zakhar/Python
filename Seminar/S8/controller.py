import view
import phonebook


def start():
    pb = phonebook.PhoneBook("phonebook.txt")
    pb_deleted = []

    while True:
        # print(pb.menu())
        choice = view.main_menu()
        # choice = int(input("Выберите пункт меню: "))
        match choice:
            case 1:
                # print(pb)
                view.show_contacts(pb, "Телефонная книга пуста")
            case 2:
                search = input("Введите строку для поиска: ")
                print(pb.find_contact(search))
            case 3:
                name = input("Введите имя: ")
                phone = input("Введите номер телефона: ")
                comment = input("Введите комментарий: ")
                pb.new_contact(name, phone, comment)
                print('Контакт добавлен!')
            case 4:
                print(pb)
                index = int(input("Выберите контакт для изменения: "))
                name = input("Введите имя: ")
                phone = input("Введите номер телефона: ")
                comment = input("Введите комментарий: ")
                pb.change_contact(index - 1, name, phone, comment)
                print('Контакт изменен!')
            case 5:
                print(pb)
                index = int(input("Выберите контакт для удаления: "))
                pb_deleted.append(pb.contacts[index - 1])
                pb.delete_contact(index - 1)
                print('Контакт успешно удален!')
            case 6:
                for i, contact in enumerate(pb_deleted, 1):
                    print(f"{i}. {contact}")
                index = int(input("Выберите контакт для восстановления: "))
                del_contact = pb_deleted[index - 1]
                pb.new_contact(del_contact.name, del_contact.phone, del_contact.comment)
                pb_deleted.pop(index - 1)
                print('Контакт успешно восстановлен!')
            case 7:
                if input("Вы хотите сохранить изменения? (y/n): ") == 'y':
                    pb.save()
            case 8:
                view.show_blue_message("Выход из программы")
                return
