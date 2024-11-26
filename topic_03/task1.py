def calculator():
    while True:
        print("Калькулятор:")
        print("Введіть операцію (+, -, *, /) або 'exit' для виходу.")
        operation = input("Операція: ")

        if operation.lower() == 'exit':
            print("Завершення роботи.")
            break

        if operation not in ('+', '-', '*', '/'):
            print("Неправильна операція. Спробуйте знову.")
            continue

        try:
            a = float(input("Перше число: "))
            b = float(input("Друге число: "))
        except:
            print("Помилка. Введіть числа.")
            continue

        if operation == '+':
            print(f"Результат: {a + b}")
        elif operation == '-':
            print(f"Результат: {a - b}")
        elif operation == '*':
            print(f"Результат: {a * b}")
        elif operation == '/':
            if b != 0:
                print(f"Результат: {a / b}")
            else:
                print("Помилка: Ділення на нуль.")

calculator()