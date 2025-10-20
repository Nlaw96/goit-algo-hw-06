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
          def __init__(self, value):
            if value is None or not value.strip():
                  raise ValueError("Phone number dont cannot empty")
            if not len(value) == 10 and not value.isdigit():
                  raise ValueError("Phone numbers must be digit")
            super().__init__(value)


class Record:
      def __init__(self, name):
            self.name = Name(name)
            self.phones = []

      def add_phone(self, number):
            phone = Phone(number)
            self.phones.append(phone)
      
      
      def remove_phone(self, value):
           for phone in self.phones:
                 if phone.value == value:
                       self.phones.remove(phone)
           raise ValueError("Phone number not found")
      
      def edit_phone(self, old_phone, new_phone):
            for phone in self.phones:
                  if phone.value == old_phone:
                        self.phones.remove(phone)
                        self.phones.append(Phone(new_phone))
                        return         
            raise ValueError("phone not found")
      
      def find_phone(self, num):
            for phone in self.phones:
                  if phone.value == num:
                        return phone
            return None
                  

      

        
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
      
phone = Phone()