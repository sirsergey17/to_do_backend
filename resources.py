import json
import os


def print_with_indent(value, indent=0):
    indentation = '\t' * indent
    print(indentation + str(value))


class Entry:
    def __init__(self, title, entries=None, parent=None):
        if entries is None:
            entries = []
        self.title = title
        self.entries = entries
        self.parent = parent

    def __str__(self):
        return self.title

    def add_entry(self, entry):
        self.entries.append(entry)
        entry.parent = self

    def print_entries(self, indent=0):
        print_with_indent(self, indent)
        for entry in self.entries:
            entry.print_entries(indent + 1)

    def json(self):
        res = {
            'title': self.title,
            'entries': []
        }
        for entry in self.entries:
            res['entries'].append(entry.json())
        return res

    @classmethod
    def from_json(cls, value: dict):
        new_entry = cls(value['title'])
        for sub_entry in value.get('entries', []):
            new_entry.add_entry(cls.from_json(sub_entry))
        return new_entry

    def save(self, path):
        full_path = os.path.join(path, f'{self.title}.json')
        with open(full_path, 'w', encoding='utf-8') as file:
            json.dump(self.json(), file)

    @classmethod
    def load(cls, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            value = json.load(file)
            return cls.from_json(value)

groceries = Entry('Продукты')
category = Entry('Мясное')

category.add_entry(Entry('Курица'))
category.add_entry(Entry('Говядина'))
category.add_entry(Entry('Колбаса'))

groceries.add_entry(category)
# groceries.print_entries()

category = Entry('Еда')

category.add_entry(Entry('Морковь'))
category.add_entry(Entry('Капуста'))

print(category.json())

# groceries.print_entries()
# groceries.save('/Users/Сергей/Wexler')
# groceries.load('/Users/Сергей/Wexler/Продукты.json')
