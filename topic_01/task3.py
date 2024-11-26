def calculate_discriminant(a, b, c):
    return b**2 - 4 * a * c

# Приклад використання
a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))

D = calculate_discriminant(a, b, c)
print("Дискримінант: ", D)
