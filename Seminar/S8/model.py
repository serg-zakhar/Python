phone_book = []
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

def get_phonebook():
    return phone_book

def add_contact(contact: dict):
    phone_book.append(contact)

