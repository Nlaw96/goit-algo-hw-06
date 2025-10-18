from dataclasses import dataclass
from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
        pass
    
class Phone(Field):
        pass

class Record:
      def __init__(self, name):
            self.name = Name(name)
            self.phones = []

        
      def __str__(self):
            return f"Contact name: {self.name.value}, phone: {";".join(p.value for p in self.phones)}"


class AdressBook(UserDict):
      def add_record(self):
            