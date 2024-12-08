class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Ім'я: {self.name}, Вік: {self.age}"

# Створення списку об'єктів Student
students = [
    Student("Олександр", 20),
    Student("Катч", 232),
    Student("Дмитро", 19),
    Student("Олександр2", 21)
]

# Сортування за віком
sorted_students = sorted(students, key=lambda student: student.age)

# Виведення відсортованих студентів
print("Сортування за віком:")
for student in sorted_students:
    print(student)
