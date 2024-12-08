
from operations4 import Operations
from userInput4 import UserInput
from logger4 import Logger

class CalculatorApp:
    def __init__(self):
        self.operations = Operations()
        self.userInput4 = UserInput()
        self.logger = Logger()

    def run(self):
        while True:
            operation = self.userInput4.select_operation()
            if operation in {'1', '2', '3', '4'}:
                a, b = self.userInput4.get_numbers()

                try:
                    if operation == '1':
                        result = self.operations.add(a, b)
                        self.logger.log_action(f"Додавання: {a} + {b} = {result}")
                    elif operation == '2':
                        result = self.operations.subtract(a, b)
                        self.logger.log_action(f"Віднімання: {a} - {b} = {result}")
                    elif operation == '3':
                        result = self.operations.multiply(a, b)
                        self.logger.log_action(f"Множення: {a} * {b} = {result}")
                    elif operation == '4':
                        result = self.operations.divide(a, b)
                        self.logger.log_action(f"Ділення: {a} / {b} = {result}")

                    print(f"Результат: {result}")
                except ZeroDivisionError as e:
                    self.logger.log_action(f"Помилка: {e}")
                    print(e)
            else:
                print("Неправильний вибір. Спробуйте ще раз.")

            again = input("\nБажаєте продовжити? (так/ні): ").strip().lower()
            if again != 'так':
                print("До побачення!")
                break

if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
