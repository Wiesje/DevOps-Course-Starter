from datetime import date, datetime


class Item:

    def __init__(self, id, name, last_modified, status='To Do'):
        self.id = id
        self.name = name
        self.status = status

    @classmethod
    def fromTrelloCard(cls, card, list):
        return cls(
            card['_id'],
            card['name'],
            list['name']
        )

    def reset(self):
        self.status = 'To Do'

    def start(self):
        self.status = 'Doing'

    def complete(self):
        self.status = 'Done'

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, status: {self.status}"

    def __eq__(self, other):
        if not isinstance(other, Item):
            return False

        return self.id == other.id \
            and self.name == other.name \
            and self.status == other.status
