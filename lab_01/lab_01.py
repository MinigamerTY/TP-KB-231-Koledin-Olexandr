list = [
    {"name":"Bob", "phone":"0631234567", "group":"KB-231", "address":"Kozatska 29"},
    {"name":"Emma", "phone":"0631234567", "group":"KB-231", "address":"Kozatska 38"},
    {"name":"Jon",  "phone":"0631234567", "group":"KB-231", "address":"Kozatska 29A"},
    {"name":"Zak",  "phone":"0631234567", "group":"KB-231", "address":"Kozatska 298"}
]

def printAllList():
    for elem in list:
        strForPrint = "Student name is " + elem["name"] + ",  Phone is " + elem["phone"] + ",  Group is " + elem["group"] + ",  Address is " + elem["address"]
        print(strForPrint)
    return

def addNewElement():
    name = input("Pease enter student name: ")
    phone = input("Please enter student phone: ")
    group = input("Pease enter student group: ")
    address = input("Please enter student address: ")
    newItem = {"name": name, "phone": phone, "group": group, "address": address}

    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Delete position " + str(deletePosition))

        del list[deletePosition]
    return


def updateElement():
    name = input("Please enter name to be updated: ")
    updatePosition = -1
    for item in list:
        if name == item["name"]:
            updatePosition = list.index(item)
            break
    if updatePosition == -1:
        print("Student not found")
    else:
        name1 = list[updatePosition]["name"]
        phone1 = list[updatePosition]["phone"]
        group1 = list[updatePosition]["group"]
        address1 = list[updatePosition]["address"]

        curinf = "Student current iformation: name — " + name1 + " , phone — " + phone1 + ", group — " + group1 + " , address — " + address1
        print(curinf)

        name = input("Enter new name or press Enter to skip:") or name1
        phone = input("Enter new phone or press Enter to skip:") or phone1
        group = input("Enter new group or press Enter to skip:") or group1
        address = input("Enter new address or press Enter to skip:") or address1
        
        if name == name1 and phone == phone1 and group == group1 and address == address1:
            print("you haven`t updated student information")
        elif name == name1:
            list[updatePosition]["phone"] = phone
            list[updatePosition]["group"] = group
            list[updatePosition]["address"] = address
        else:
            updatedItem = {"name": name, "phone": phone, "group": group, "address": address}
            del list[updatePosition]
            insertPosition = 0
            for item in list:
                if name > item["name"]:
                    insertPosition += 1

            list.insert(insertPosition, updatedItem)
        print("information has been updated")
    return


def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
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
                print("Exit()")
                break
            case _:
                print("Wrong chouse")


main()