from functions import add, subtract, multiply, divide
from operations import get_numbers, select_operation

def main():
    while True:
        operation = select_operation()
        if operation in {'1', '2', '3', '4'}:
            a, b = get_numbers()

            if operation == '1':
                print(f"Результат: {add(a, b)}")
            elif operation == '2':
                print(f"Результат: {subtract(a, b)}")
            elif operation == '3':
                print(f"Результат: {multiply(a, b)}")
            elif operation == '4':
                try:
                    print(f"Результат: {divide(a, b)}")
                except ValueError as e:
                    print(e)
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

        again = input("Бажаєте продовжити? (так/ні): ").lower()
        if again != 'так':
            print("До побачення!")
            break

if __name__ == "__main__":
    main()
