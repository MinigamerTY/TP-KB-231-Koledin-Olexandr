import os
import csv
from sys import argv

# Определяем путь к файлу по умолчанию в той же папке, где находится скрипт
BASE_DIR = os.path.dirname(__file__)  # Получаем директорию текущего файла
DEF_NAME = os.path.join(BASE_DIR, "lab_02.csv")  # lab_02.csv в папке с программой

students = []

def printAllList():
    if not students:
        print("The list of students is empty")
        return
    for elem in students:
        strForPrint = (
            "Student name is " + elem["name"] +
            ",  Phone is " + elem["phone"] +
            ",  Group is " + elem["group"] +
            ",  Address is " + elem["address"]
        )
        print(strForPrint)
    return

def addNewElement():
    name = input("Please enter student name: ") or "Unknown"
    phone = input("Please enter student phone: ") or "Unknown"
    group = input("Please enter student group: ") or "Unknown"
    address = input("Please enter student address: ") or "Unknown"
    newItem = {"name": name, "phone": phone, "group": group, "address": address}
    insertPosition = 0
    for item in students:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    students.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in students:
        if name == item["name"]:
            deletePosition = students.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Delete position " + str(deletePosition))
        del students[deletePosition]
    return

def updateElement():
    name = input("Please enter name to be updated: ")
    updatePosition = -1
    for item in students:
        if name == item["name"]:
            updatePosition = students.index(item)
            break
    if updatePosition == -1:
        print("Student not found")
    else:
        name1 = students[updatePosition]["name"]
        phone1 = students[updatePosition]["phone"]
        group1 = students[updatePosition]["group"]
        address1 = students[updatePosition]["address"]

        curinf = (
            "Student current information: name — " + name1 +
            " , phone — " + phone1 +
            ", group — " + group1 +
            " , address — " + address1
        )
        print(curinf)

        name = input("Enter new name or press Enter to skip:") or name1
        phone = input("Enter new phone or press Enter to skip:") or phone1
        group = input("Enter new group or press Enter to skip:") or group1
        address = input("Enter new address or press Enter to skip:") or address1
        
        if name == name1 and phone == phone1 and group == group1 and address == address1:
            print("You haven't updated student information")
        elif name == name1:
            students[updatePosition]["phone"] = phone
            students[updatePosition]["group"] = group
            students[updatePosition]["address"] = address
        else:
            updatedItem = {"name": name, "phone": phone, "group": group, "address": address}
            del students[updatePosition]
            insertPosition = 0
            for item in students:
                if name > item["name"]:
                    insertPosition += 1

            students.insert(insertPosition, updatedItem)
        print("Information has been updated")
    return

def import_data(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({
                    "name": row.get("name", "Unknown"), 
                    "phone": row.get("phone", "Unknown"), 
                    "group": row.get("group", "Unknown"), 
                    "address": row.get("address", "Unknown")
                })
    except FileNotFoundError:
        print(f"File '{file_name}' not found \nThe initial list will be empty")
    except Exception as e:
        print(f"File loading error: {e}")

def save_data(file_name):
    try:
        with open(file_name, 'w', encoding='utf-8', newline='') as file:
            fieldnames = ["name", "phone", "group", "address"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students)
        print(f"Data successfully saved to '{file_name}'")
    except Exception as e:
        print(f"File saving error: {e}")

def main():
    if len(argv) == 1:
        data_file = DEF_NAME
    else:
        data_file = os.path.join(BASE_DIR, argv[1])  # Используем файл, указанный в аргументах
    
    print(f"File used '{data_file}'")
    import_data(data_file)

    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                save_data(data_file)
                print("Exit()")
                break
            case _:
                print("Wrong choice")


main()