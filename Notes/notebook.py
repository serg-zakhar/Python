import datetime


# import json
# import csv


class Note:

    def __init__(self, n_id: int, header: str, content: str, date: str):
        self.n_id = n_id
        self.header = header
        self.content = content
        self.date = date

    def to_string(self):
        return f'{self.n_id};{self.header};{self.content};{self.date}'

    def __str__(self):
        return f"{self.n_id}. {self.header}\n| {self.content} |\n{self.date}"


class Notebook:

    def __init__(self, path: str):
        self.path = path
        self.notes = []
        self.open()

    def __str__(self):
        result = ''
        for note in self.notes:
            result += f'{note}\n'
        return result

    def open(self):
        with open(self.path, 'r', encoding="UTF-8") as file:
            notes = file.readlines()
        for note in notes:
            new_note = note.strip().split(';')
            self.notes.append(Note(*new_note))
        # with open(self.path, 'r', newline='') as f:
        #     notes = csv.reader(f, delimiter=';')
        #     for row in notes:
        #         note = Note(int(row[0]), row[1], row[2], row[3])
        #         self.notes.append(note)
        # with open(self.path, 'r') as fh:
        # notes = json.load(fh)

    def new_note(self, n_id: int, header: str, content: str, date: datetime):
        self.notes.append(Note(n_id, header, content, date))

    def save(self):
        data = '\n'.join([note.to_string() for note in self.notes])
        with open(self.path, 'w', encoding="UTF-8") as file:
            file.write(data)
        # with open(self.path, 'w', newline='') as f:
        #     writer = csv.writer(f, delimiter=";")
        #     # for row in data:
        #     writer.writerows(data)

    def change_note(self, n_id: int, header: str, content: str):
        header = header if header != '' else self.notes[n_id].header
        content = content if content != '' else self.notes[n_id].content
        dt = datetime.datetime.today().strftime("%d/%m/%Y %H:%M")
        self.notes[n_id - 1] = Note(n_id, header, content, dt)

    def delete_note(self, n_id: int):
        self.notes.pop(n_id)
