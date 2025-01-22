from typing import List
from resources import Entry
import os


class EntryManager:
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.entries = []

    def save(self):
        for item in self.entries:
            item.save(self.data_path)

    def load(self):
        if not os.path.isdir(self.data_path):
            os.makedirs(self.data_path)
        else:
            for line in os.listdir(self.data_path):
                full_path = os.path.join(self.data_path, line)
                if full_path.endswith('json'):
                    x = Entry.load(full_path)
                    self.entries.append(x)
        return self

    def add_entry(self, title: str):
        new_entry = Entry(title)
        self.entries.append(new_entry)