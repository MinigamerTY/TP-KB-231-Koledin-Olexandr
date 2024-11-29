from functions import add, subtract, multiply, divide
from operations import get_numbers, select_operation

# Функція для запису логів у файл
def log_action(message):
    with open("calculator_log.txt", "a") as log_file:
        log_file.write(message + "\n")

def main():
    while True:
        operation = select_operation()
        if operation in {'1', '2', '3', '4'}:
            a, b = get_numbers()

            try:
                if operation == '1':
                    result = add(a, b)
                    log_action(f"Додавання: {a} + {b} = {result}")
                elif operation == '2':
                    result = subtract(a, b)
                    log_action(f"Віднімання: {a} - {b} = {result}")
                elif operation == '3':
                    result = multiply(a, b)
                    log_action(f"Множення: {a} * {b} = {result}")
                elif operation == '4':
                    result = divide(a, b)
                    log_action(f"Ділення: {a} / {b} = {result}")

                print(f"Результат: {result}")
            except ValueError as e:
                log_action(f"Помилка: {e}")
                print(e)
        else:
            log_action("Неправильний вибір операції")
            print("Неправильний вибір. Спробуйте ще раз.")

        again = input("\nБажаєте продовжити? (так/ні): ").strip().lower()
        if again != 'так':
            log_action("Програма завершена користувачем.")
            print("До побачення!")
            break




