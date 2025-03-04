import math

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None  # Нет действительных корней
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    return x1, x2

# Коэффициенты уравнения
a = 1.0
b = 0.4002
c = 0.00008

# Решение с 4-мя знаками после запятой
b_4 = round(b, 4)
c_4 = round(c, 4)
x1_4, x2_4 = solve_quadratic(a, b_4, c_4)

# Решение с 8-ю знаками после запятой
b_8 = round(b, 8)
c_8 = round(c, 8)
x1_8, x2_8 = solve_quadratic(a, b_8, c_8)

# Вычисление абсолютной и относительной погрешностей
def calculate_errors(x_approx, x_exact):
    absolute_error = abs(x_approx - x_exact)
    relative_error = absolute_error / abs(x_exact) if x_exact != 0 else None
    return absolute_error, relative_error


def four():
    abs_error_x1, rel_error_x1 = calculate_errors(x1_4, x1_8)

    abs_error_x2, rel_error_x2 = calculate_errors(x2_4, x2_8)
    print("Задание 4:")
    print(f"Решение с 4-мя знаками: x1 = {x1_4:.8f}, x2 = {x2_4:.8f}")
    print(f"Решение с 8-ю знаками: x1 = {x1_8:.8f}, x2 = {x2_8:.8f}")
    print(f"Абсолютная погрешность для x1: {abs_error_x1:.8f}")
    print(f"Относительная погрешность для x1: {rel_error_x1:.8f}")
    print(f"Абсолютная погрешность для x2: {abs_error_x2:.8f}")
    print(f"Относительная погрешность для x2: {rel_error_x2:.8f}")
    print()