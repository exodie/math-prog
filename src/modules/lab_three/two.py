import numpy as np

# Исходные данные
x = np.array([0.50, 0.75, 1.00, 1.25, 1.50])
y = np.array([1.732, 2.280, 3.000, 3.948, 5.196])

def divided_diff(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    coef[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])

    return coef

def newton_poly(coef, x_data, x_val):
    n = len(coef) - 1
    p = coef[n]
    for k in range(1, n + 1):
        p = coef[n - k] + (x_val - x_data[n - k]) * p
    return p

def two():
    coef = divided_diff(x, y)[0, :]

    x_val = 1.30
    y_val = newton_poly(coef, x, x_val)

    true_value = np.sqrt(x_val)
    error = abs(y_val - true_value)

    print("Задание 2")
    print(f"Значение функции в точке x = {x_val}: {y_val}")
    print(f"Истинное значение функции в точке x = {x_val}: {true_value}")
    print(f"Погрешность: {error}")