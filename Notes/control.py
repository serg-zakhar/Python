import datetime
import notebook
import view


def start():
    nb = notebook.Notebook("notes.txt")

    while True:
        choice = view.main_menu()
        match choice:
            case 1:  # Показать все заметки
                view.show_notes(nb, "Заметки отсутствуют")
            case 2:  # Найти заметку
                search = nb.find_contact(view.input_search("Введите строку для поиска: "))
                view.show_notes(search, "Заметки не найдены")
            case 3:  # Добавить заметку
                n_id = len(nb.notes) + 1
                nb.new_note(*view.add_note(n_id))
                view.show_blue_message('Заметка добавлена!')
            case 4:  # Изменить заметку
                view.show_notes(nb, "Заметки отсутствуют")
                index = view.input_index("Выберите заметку для изменения: ")
                if index and 0 < index <= len(nb.contacts):
                    nb.change_contact(index - 1, *view.change_contact(nb))
                    view.show_blue_message(f"заметку {index} изменен")
                else:
                    view.show_red_message("Введен некорректный номер заметки")
            case 5:  # Удалить заметку
                view.show_notes(nb, "Заметки отсутствуют")
                index = view.input_index("Выберите заметку для удаления: ")
                if index and 0 < index <= len(nb.contacts):
                    nb_deleted.append(nb.contacts[index - 1])
                    nb.delete_contact(index - 1)
                    view.show_blue_message('Заметка успешно удалена!')
                else:
                    view.show_red_message("Введен некорректный номер заметки")
            case 6:  # Восстановить заметку
                view.show_notes(nb_deleted, "Отсутствуют заметки для восстановления")
                index = view.input_index("Выберите заметку для восстановления: ")
                if index and 0 < index <= len(nb_deleted):
                    del_contact = nb_deleted[index - 1]
                    nb.new_contact(del_contact.name, del_contact.phone, del_contact.comment)
                    nb_deleted.pop(index - 1)
                    view.show_blue_message('Заметка успешно восстановлена!')
                else:
                    view.show_red_message("Введен некорректный номер заметки")
            case 7:  # Сохранить изменения
                if view.input_choice("Вы хотите сохранить изменения? (y/n): ") == "y":
                    nb.save()
                    view.show_blue_message("Заметки успешно сохранены")
                else:
                    view.show_red_message("Заметки не сохранены")
            case 8:  # Выход
                if view.input_choice("Вы хотите сохранить изменения перед выходом? (y/n): ") == "y":
                    nb.save()
                    view.show_blue_message("Заметки успешно сохранены")
                    view.show_blue_message("Выход из программы")
                    return
                else:
                    view.show_blue_message("Выход из программы")
                    return

    # view.show_notes(nb, "Заметки отсутствуют")