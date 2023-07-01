import datetime
import notebook
import view


def start():
    nb = notebook.Notebook("notes.txt")
    nb_deleted = []

    while True:
        choice = view.main_menu()
        match choice:
            case 1:  # Показать все заметки
                view.show_notes(nb, "Заметки отсутствуют")
            case 2:  # Найти заметку
                sub_choice = view.sub_menu()
                if sub_choice == 1:
                    search = nb.find_note(view.input_search("Введите строку для поиска: "))
                    view.show_notes(search, "Заметки не найдены")
                elif sub_choice == 2:


            case 3:  # Добавить заметку
                n_id = len(nb.notes) + 1
                nb.new_note(*view.add_note(n_id))
                view.show_blue_message('Заметка добавлена!')
            case 4:  # Изменить заметку
                view.show_notes(nb, "Заметки отсутствуют")
                index = view.input_index("Выберите заметку для изменения: ")
                if index and 0 < index <= len(nb.notes):
                    note = view.change_note(index)
                    nb.change_note(index, note[1], note[2])
                    view.show_blue_message(f"заметка {index} изменена")
                else:
                    view.show_red_message("Введен некорректный номер заметки")
            case 5:  # Удалить заметку
                view.show_notes(nb, "Заметки отсутствуют")
                index = view.input_index("Выберите заметку для удаления: ")
                if index and 0 < index <= len(nb.notes):
                    n_id_delnote = len(nb_deleted) + 1
                    print(n_id_delnote)
                    nb.notes[index - 1].n_id = n_id_delnote
                    nb_deleted.append(nb.notes[index - 1])
                    nb.delete_note(index - 1)
                    nb.change_id()
                    view.show_blue_message('Заметка успешно удалена!')
                else:
                    view.show_red_message("Введен некорректный номер заметки")
            case 6:  # Восстановить заметку
                view.show_delnotes(nb_deleted, "Отсутствуют заметки для восстановления")
                if nb_deleted:
                    index = view.input_index("Выберите заметку для восстановления: ")
                    if index and 0 < index <= len(nb_deleted):
                        del_note = nb_deleted[index - 1]
                        nb.new_note(del_note.n_id, del_note.header, del_note.content, del_note.date)
                        nb_deleted.pop(index - 1)
                        nb.change_id()
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
                if view.input_choice("Вы хотите сохранить изменения перед выходом? (y/n):") == "y":
                    nb.save()
                    view.show_blue_message("Заметки успешно сохранены")
                    view.show_blue_message("Выход из программы")
                    return
                else:
                    view.show_red_message("Изменения не сохранены!")
                    view.show_blue_message("Выход из программы")
                    return

