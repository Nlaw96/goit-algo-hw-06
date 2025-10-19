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
      def add_record(self, record):
            self.data[record.name.value] = record


            
      def find(self, items):
            if items in self.data.keys():
                  return self.data[items]
            for row in self.data.values():
                  for phone in row.phones:
                        if phone == items:
                              return row
            return None
            

      
      def delete(self, name):
            if name in self.data.keys():
                  self.data.pop(name)
            return None
      def __str__(self):
            return super().__str__(self.data)