import datetime


class Note:

    def __init__(self, header: str, content: str, date: datetime):
        self.header = header
        self.content = content
        self.date = date

    def to_string(self):
        return f'{self.header} {self.content} {self.date}'


class Notebook:

    def __init__(self, path: str):
        self.path = path
        self.notes = []
        self.open()


