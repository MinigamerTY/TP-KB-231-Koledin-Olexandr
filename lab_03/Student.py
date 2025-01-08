class Student:
    def __init__(self, name, phone, group, address):
        self.name = name
        self.phone = phone
        self.group = group
        self.address = address

    def __str__(self):
        return f"Student name: {self.name}, Phone: {self.phone}, Group: {self.group}, Address: {self.address}"
