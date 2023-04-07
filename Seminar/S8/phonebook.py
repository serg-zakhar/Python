class Contact:

    def __init__(self, name: str, phone: str, comment: str):
        self.name = name
        self.phone = phone
        self.comment = comment

    def __str__(self):
        return f"{self.name} | {self.phone} | {self.comment}"


class PhoneBook:

    def __int__(self, path: str):
        self.path = path
        self.contacts = []
        self.open()

    def open(self):
        with open(self.path, 'r', encoding="UTF-8") as file:
            contacts = file.readlines()
        for contact in contacts:
            new_contact = contact.strip().split(';')
            self.contacts.append(Contact(*new_contact))

    def __str__(self):
        return '\n'.join(self.contacts)
