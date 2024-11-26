def test_list():
    my_list = [1,50,56,21,14,18,15,10,10,10,6,88]
    print("Тестування функцій списків:")

    #створює копію списку, не змінюючи оригінальний список
    copy_list = my_list.copy()
    print("copy():", copy_list)

    #додає 3 в кінець списку
    my_list.append(3)
    print("append(3):", my_list)


    #додає числа в кінец існуючого ссписку
    my_list.extend([10, 15])
    print("extend([10, 15]):", my_list)

    #вставляє число 7 на позицію з індексом 1 
    my_list.insert(1, 7)
    print("insert(1, 7):", my_list)

    #видаляє перший раз 10 з спсику
    my_list.remove(10)
    print("remove(10):", my_list)

    #перевертає список
    my_list.reverse()
    print("reverse():", my_list)

    #сортує список за зростанням
    my_list.sort()
    print("sort():", my_list)

    #очищає список, видаляючи всі елементи
    my_list.clear()
    print("clear():", my_list)

test_list()