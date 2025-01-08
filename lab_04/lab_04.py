# Функція для переведення виразу в ЗПН
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0, ')': 0}
    stack = []
    postfix = []

    for char in expression:
        if char.isnumeric():  # Якщо це операнд (число)
            postfix.append(char)
        elif char == '(':  # Якщо це ліва дужка
            stack.append(char)
        elif char == ')':  # Якщо це права дужка
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # Викидаємо '('
        else:  # Якщо це оператор
            while stack and precedence[char] <= precedence.get(stack[-1], 0):
                postfix.append(stack.pop())
            stack.append(char)

    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix)


# Функція для обчислення результату виразу в ЗПН
def evaluate_postfix(expression):
    stack = []

    for char in expression:
        if char.isnumeric():  # Якщо це операнд
            stack.append(int(char))
        else:  # Якщо це оператор
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a / b)

    return stack.pop()

expression = input("Введіть інфіксний вираз: ")
    
# Перетворюємо вираз у ЗПН
postfix = infix_to_postfix(expression)
print(f"Вираз у ЗПН: {postfix}")
    
# Обчислюємо результат
result = evaluate_postfix(postfix)
print(f"Результат: {result}")
