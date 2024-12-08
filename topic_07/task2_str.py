class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Ім'я: {self.name}, Вік: {self.age}"

# Створення об'єкта
human = Person("Олександр", 30)
print(human) 
 