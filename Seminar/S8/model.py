import controller
phone_book = []
del_phone_book = []
path = "phonebook.txt"


def open_phonebook():
    with open(path, 'r', encoding="UTF-8") as file:
        list_phonebook = file.readlines()
        for fields in list_phonebook:
            fields = fields.strip().split(";")
            contact = {'name': fields[0],
                       'phone': fields[1],
                       'comment': fields[2]}
            phone_book.append(contact)
    controller.pb_opened = True

def save_phonebook():
    data = []
    for contact in phone_book:
        data.append(";".join(list(contact.values())))
    data = "\n".join(data)
    with open(path, 'w', encoding="UTF-8") as file:
        file.write(data)


def get_phonebook():
    return phone_book


def add_contact(contact: dict):
    phone_book.append(contact)


def change_contact(contact: dict, index: int):
    phone_book.pop(index - 1)
    phone_book.insert(index - 1, contact)


def find_contact(search: str):
    result = []
    for contact in phone_book:
        for field in contact.values():
            if search.lower() in field.lower():
                result.append(contact)
    return result


def delete_contact(index: int):
    del_phone_book.append(phone_book[index - 1])
    phone_book.pop(index - 1)

def restore_contact(index: int):
    phone_book.append(del_phone_book[index - 1])
    del_phone_book.pop(index - 1)

