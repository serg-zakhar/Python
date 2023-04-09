class Contact:

    def __init__(self, name: str, phone: str, comment: str):
        self.name = name
        self.phone = phone
        self.comment = comment

    def to_string(self):
        return f'{self.name}: {self.phone}, {self.comment}'


    def __str__(self):
        return f"{self.name:<20} | {self.phone:<20} | {self.comment:<20}"


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

    def save(self):
        data = '\n'.join([contact.to_string() for contact in self.contacts])
        with open(self.path, 'w', encoding="UTF-8") as file:
            file.write(data)

    def new_contact(self, name: str, phone: str, comment: str):
        self.contacts.append(Contact(name, phone, comment))


    def __str__(self):
        result = ''
        for contact in self.contacts:
            result += f'{contact}\n'
        return result
