
class UserInput:
    def get_numbers(self):
        while True:
            try:
                a = float(input("Введіть перше число: "))
                b = float(input("Введіть друге число: "))
                return a, b
            except ValueError:
                print("Будь ласка, введіть коректні числа.")

    def select_operation(self):
        print("Оберіть операцію:")
        print("1 - Додавання")
        print("2 - Віднімання")
        print("3 - Множення")
        print("4 - Ділення")
        operation = input("Ваш вибір: ")
        return operation
