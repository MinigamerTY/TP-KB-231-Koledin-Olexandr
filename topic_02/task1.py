def calculate_discriminant(a, b, c):
    #Функція для обчислення дискримінанта квадратного рівняння
    return b**2 - 4 * a * c

def find_roots(a, b, c):
    #Функція для пошуку коренів квадратного рівняння
    D = calculate_discriminant(a, b, c)
    
    if D > 0:
        x1 = (-b + D**0.5) / (2 * a)
        x2 = (-b - D**0.5) / (2 * a)
        print("Корені: x1 =", x1, "x2 =", x2)
    elif D == 0:
        x = -b / (2 * a)
        print("Єдиний корінь: x =", x)
    else:
        print("Немає дійсних коренів.")

# Введення даних
a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))

find_roots(a, b, c)
