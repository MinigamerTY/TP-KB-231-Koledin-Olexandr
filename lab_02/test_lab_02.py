import unittest
import unittest.mock
from io import StringIO
import sys
import os
import tempfile
import csv

from lab_02 import students, addNewElement, deleteElement, updateElement, import_data, save_data, printAllList


class TestStudentList(unittest.TestCase):
    def setUp(self):
        self.test_file = tempfile.NamedTemporaryFile('w', encoding='utf-8', newline='', delete=False)
        self.test_file_name = self.test_file.name
        self.test_file.close()
        students.clear()

    def tearDown(self):
        if os.path.exists(self.test_file_name):
            os.remove(self.test_file_name)

    def test_addNewElement(self):
        input_data = ["Test Student", "0933752088", "KB-231", "Kozatska63"]

        with unittest.mock.patch('builtins.input', side_effect=input_data):
            addNewElement()

        self.assertEqual(len(students), 1)
        self.assertEqual(students[0]['name'], "Test Student")
        self.assertEqual(students[0]['phone'], "0933752088")
        self.assertEqual(students[0]['group'], "KB-231")
        self.assertEqual(students[0]['address'], "Kozatska63")

    def test_deleteElement(self):
        students.append({"name": "Test Student", "phone": "0933752088", "group": "KB-231", "address": "Kozatska63"})

        with unittest.mock.patch('builtins.input', return_value="Test Student"):
            deleteElement()

        self.assertEqual(len(students), 0)

    def test_updateElement(self):
        students.append({"name": "Test Student", "phone": "0933752088", "group": "KB-231", "address": "Kozatska63"})
        input_data = ["Test Student", "Updated Student", "0666666666", "KB-232", "Kozatska66"]

        with unittest.mock.patch('builtins.input', side_effect=input_data):
            updateElement()

        self.assertEqual(len(students), 1)
        self.assertEqual(students[0]['name'], "Updated Student")
        self.assertEqual(students[0]['phone'], "0666666666")
        self.assertEqual(students[0]['group'], "KB-232")
        self.assertEqual(students[0]['address'], "Kozatska66")

    def test_import_data(self):
        data = [
            {"name": "Sasha1", "phone": "0664567891", "group": "KB-231", "address": "Kozatska1"},
            {"name": "Sasha2", "phone": "0661231321", "group": "KB-231", "address": "Kozatska2"}
        ]

        with open(self.test_file_name, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "phone", "group", "address"])
            writer.writeheader()
            writer.writerows(data)

        import_data(self.test_file_name)
        
        self.assertEqual(len(students), 2)
        self.assertEqual(students[0]['name'], "Sasha1")
        self.assertEqual(students[1]['name'], "Sasha2")
        self.assertEqual(students[0]['group'], "KB-231")
        self.assertEqual(students[1]['group'], "KB-231")

    def test_save_data(self):
        students.append({"name": "Chris", "phone": "0663335554", "group": "KB-231", "address": "Kozatska3"})
        save_data(self.test_file_name)

        with open(self.test_file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            rows = list(reader)

            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["name"], "Chris")
            self.assertEqual(rows[0]['phone'], "0663335554")
            self.assertEqual(rows[0]['group'], "KB-231")
            self.assertEqual(rows[0]['address'], "Kozatska3")

    def test_printAllList(self):
        students.append({"name": "Test Student", "phone": "0663335554", "group": "KB-231", "address": "Kozatska14"})
        captured_output = StringIO()
        sys.stdout = captured_output
        printAllList()
        sys.stdout = sys.__stdout__

        self.assertIn("Test Student", captured_output.getvalue())



    unittest.main()
