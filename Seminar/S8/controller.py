import view
import model

def start():
    while True:
        num_menu = view.main_menu()
        match num_menu:
            case 1:
                model.open_phonebook()
            case 2:
                pass
            case 3:
                pb = model.get_phonebook()
                view.show_contacts(pb, "Телефонная книга пуста или не открыта")
            case 4:
                pass
            case 5:
                model.add_contact(view.add_contact())
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case _:
                pass
