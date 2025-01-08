import unittest
from Student import Student
from StudentList import StudentList
from Utils import Utils
import tempfile
import os

class TestStudentList(unittest.TestCase):
    def setUp(self):
        self.student_list = StudentList()

    def test_add_student(self):
        self.student_list.add_student("Sasha", "0661234567", "KB-231", "Kozatska 15")
        self.assertEqual(len(self.student_list.students), 1)

    def test_delete_student(self):
        self.student_list.add_student("Marina", "0667654321", "KB-231", "Kozatska 16")
        self.student_list.delete_student("Marina")
        self.assertEqual(len(self.student_list.students), 0)

    def test_update_student(self):
        self.student_list.add_student("Charlie", "0660000000", "KB-231", "Kozatska 17")
        self.student_list.update_student("Charlie", phone="0661111111")
        self.assertEqual(self.student_list.students[0].phone, "0661111111")

    def test_save_and_import_data(self):
        with tempfile.NamedTemporaryFile('w', delete=False) as temp_file:
            file_name = temp_file.name
        Utils.save_data(file_name, self.student_list)
        new_list = StudentList()
        Utils.import_data(file_name, new_list)
        os.remove(file_name)
        self.assertEqual(len(new_list.students), len(self.student_list.students))

if __name__ == "__main__":
    unittest.main()
