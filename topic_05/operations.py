def get_numbers():
    try:
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
        return a, b
    except ValueError:
        print("Будь ласка, вводьте лише числа.")
        return get_numbers()

def select_operation():
    print("Оберіть операцію:")
    print("1 - Додавання")
    print("2 - Віднімання")
    print("3 - Множення")
    print("4 - Ділення")
    return input("Ваш вибір: ")
