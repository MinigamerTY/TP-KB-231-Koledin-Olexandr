import os
from StudentList import StudentList
from Utils import Utils

BASE_DIR = os.path.dirname(__file__)
DEF_NAME = os.path.join(BASE_DIR, "lab_03.csv")

def main():
    student_list = StudentList()

    # Зчитування даних з файлу
    Utils.import_data(DEF_NAME, student_list)

    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ").lower()
        match choice:
            case "c":
                name = input("Enter student name: ")
                phone = input("Enter student phone: ")
                group = input("Enter student group: ")
                address = input("Enter student address: ")
                student_list.add_student(name, phone, group, address)
            case "u":
                name = input("Enter the name of the student to update: ")
                new_name = input("Enter new name or press Enter to skip: ")
                phone = input("Enter new phone or press Enter to skip: ")
                group = input("Enter new group or press Enter to skip: ")
                address = input("Enter new address or press Enter to skip: ")
                if not student_list.update_student(name, new_name, phone, group, address):
                    print("Student not found.")
            case "d":
                name = input("Enter the name of the student to delete: ")
                if not student_list.delete_student(name):
                    print("Student not found.")
            case "p":
                student_list.print_all_students()
            case "x":
                Utils.save_data(DEF_NAME, student_list)
                print("Exiting program.")
                break
            case _:
                print("Invalid choice.")


main()

