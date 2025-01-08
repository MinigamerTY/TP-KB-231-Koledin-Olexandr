from Student import Student

class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, name, phone, group, address):
        student = Student(name, phone, group, address)
        self.students.append(student)
        self.students.sort(key=lambda x: x.name)

    def delete_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                return True
        return False

    def update_student(self, name, new_name=None, phone=None, group=None, address=None):
        for student in self.students:
            if student.name == name:
                student.name = new_name or student.name
                student.phone = phone or student.phone
                student.group = group or student.group
                student.address = address or student.address
                self.students.sort(key=lambda x: x.name)
                return True
        return False

    def print_all_students(self):
        if not self.students:
            print("The list of students is empty.")
        else:
            for student in self.students:
                print(student)
