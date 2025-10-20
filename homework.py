from dataclasses import dataclass
from collections import UserDict

class Field:
    def __init__(self, value):
        #store the value of the field
        self.value = value

    def __str__(self):
        #return the field value
        return str(self.value)

class Name(Field):
        # use the constructore for the parent class
        def __init__(self, value):
              super().__init__(value)

        def __str__(self):
              #return name value
              return super().__str__()
      
class Phone(Field):
          def __init__(self, value):
            #validation phone cannot be empty
            if value is None or not value.strip():
                  raise ValueError("Phone number  cannot be empty")
            if not len(value) == 10 or not value.isdigit():
                  raise ValueError("Phone numbers must be digit")
            super().__init__(value)


class Record:
      def __init__(self, name):
            self.name = Name(name)
            self.phones = []

      #add new phone namber
      def add_phone(self, number):
            phone = Phone(number)
            self.phones.append(phone)
      
      #remove phone number
      def remove_phone(self, value):
           for phone in self.phones:
                 if phone.value == value:
                       self.phones.remove(phone)
                       return
           raise ValueError("Phone number not found")
      
      #replace an old number with a new one
      def edit_phone(self, old_phone, new_phone):
            for phone in self.phones:
                  if phone.value == old_phone:
                        self.phones.remove(phone)
                        self.phones.append(Phone(new_phone))
                        return         
            raise ValueError("phone not found")
      
      #find a phone in the contact
      def find_phone(self, num):
            for phone in self.phones:
                  if phone.value == num:
                        return phone
            return None
      #formated output for the contact
      def __str__(self):
            return f"Contact name: {self.name.value}, phone: {';'.join(p.value for p in self.phones)}"
      
#---------    
#class for the address book
#---------
class AddressBook(UserDict):
      def add_record(self, record):
            self.data[record.name.value] = record


      #find the record by name   
      def find(self, name):
            if name not in  self.data:
                  return None
            return self.data.get(name)
            

      #delete a record by name
      def delete(self, name):
            self.data.pop(name, None)

      #formatted record for the addressbook
      def __str__(self):
            if not self.data:
                  return "AddressBook is empty"
            records = ["  " + str(record) for record in self.data.values()]
            return "AddressBook:\n" + "\n".join(records) 
      
#create addressbook  
book = AddressBook()

 # creatr record for  John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

    # Added record for John to address book
book.add_record(john_record)

    # create and recording a new record for  Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

    # print all record in a book
     
print(book)

    # find and edit phone numbers for  John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Print: Contact name: John, phones: 1112223333; 5555555555

    # Search specific record in John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

    # Delete Jane
book.delete("Jane")
