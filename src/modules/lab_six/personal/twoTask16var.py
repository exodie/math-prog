import numpy as np

# Заданные данные
x = np.array([0.2, 0.4, 0.5])
y = np.array([0.45, 0.63, 0.70])

# Точка, в которой нужно найти производные
x2 = 0.4

# Интерполяция многочленом Лагранжа
def lagrange_poly(x, y, xi):
    n = len(x)
    result = 0.0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term *= (xi - x[j]) / (x[i] - x[j])
        result += term
    return result

# Производная многочлена Лагранжа
def lagrange_derivative(x, y, xi):
    n = len(x)
    result = 0.0
    for i in range(n):
        sum_term = 0.0
        for j in range(n):
            if i != j:
                term = 1.0 / (x[i] - x[j])
                for k in range(n):
                    if k != i and k != j:
                        term *= (xi - x[k]) / (x[i] - x[k])
                sum_term += term
        result += y[i] * sum_term
    return result

# Вторая производная многочлена Лагранжа
def lagrange_second_derivative(x, y, xi):
    n = len(x)
    result = 0.0
    for i in range(n):
        sum_term = 0.0
        for j in range(n):
            if i != j:
                for k in range(n):
                    if k != i and k != j:
                        term = 1.0 / ((x[i] - x[j]) * (x[i] - x[k]))
                        for l in range(n):
                            if l != i and l != j and l != k:
                                term *= (xi - x[l]) / (x[i] - x[l])
                        sum_term += term
        result += y[i] * sum_term
    return result

# Интерполяция многочленом Ньютона
def newton_poly(x, y, xi):
    n = len(x)
    a = y.copy()
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            a[i] = (a[i] - a[i-1]) / (x[i] - x[i-j])
    result = a[n-1]
    for i in range(n-2, -1, -1):
        result = result * (xi - x[i]) + a[i]
    return result

# Производная многочлена Ньютона
def newton_derivative(x, y, xi):
    n = len(x)
    a = y.copy()
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            a[i] = (a[i] - a[i-1]) / (x[i] - x[i-j])
    result = a[1] + a[2] * (2 * xi - x[0] - x[1])
    return result

# Вторая производная многочлена Ньютона
def newton_second_derivative(x, y, xi):
    n = len(x)
    a = y.copy()
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            a[i] = (a[i] - a[i-1]) / (x[i] - x[i-j])
    result = 2 * a[2]
    return result

# Вычисление производных
y_prime_lagrange = lagrange_derivative(x, y, x2)
y_double_prime_lagrange = lagrange_second_derivative(x, y, x2)

y_prime_newton = newton_derivative(x, y, x2)
y_double_prime_newton = newton_second_derivative(x, y, x2)

# Вывод результатов
print(f"Производная в точке x2 = {x2} (Лагранж): {y_prime_lagrange}")
print(f"Вторая производная в точке x2 = {x2} (Лагранж): {y_double_prime_lagrange}")
print(f"Производная в точке x2 = {x2} (Ньютон): {y_prime_newton}")
print(f"Вторая производная в точке x2 = {x2} (Ньютон): {y_double_prime_newton}")