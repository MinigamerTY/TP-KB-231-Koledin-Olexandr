import csv
from Student import Student

class Utils:
    @staticmethod
    def import_data(file_name, student_list):
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student_list.add_student(
                        row.get("name", "Unknown"),
                        row.get("phone", "Unknown"),
                        row.get("group", "Unknown"),
                        row.get("address", "Unknown")
                    )
        except FileNotFoundError:
            print(f"File '{file_name}' not found. Starting with an empty list.")
        except Exception as e:
            print(f"File loading error: {e}")

    @staticmethod
    def save_data(file_name, student_list):
        try:
            with open(file_name, 'w', encoding='utf-8', newline='') as file:
                fieldnames = ["name", "phone", "group", "address"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for student in student_list.students:
                    writer.writerow({
                        "name": student.name,
                        "phone": student.phone,
                        "group": student.group,
                        "address": student.address
                    })
            print(f"Data successfully saved to '{file_name}'")
        except Exception as e:
            print(f"File saving error: {e}")
