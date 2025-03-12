import numpy as np


def divided_diff(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    coef[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])

    return coef[0, :]  # Возвращаем первую строку коэффициентов


def newton_poly(coef, x_data, x):
    n = len(coef) - 1
    p = coef[n]
    for k in range(1, n + 1):
        p = coef[n - k] + (x - x_data[n - k]) * p
    return p


# Данные из варианта 16
x_r = 0.335
x = np.array([0.27])
y = np.array([6.0496])

# Вычисляем коэффициенты разделенных разностей
coef = divided_diff(x, y)

# Вычисляем значение интерполяционного многочлена в точке x_r
y_r = newton_poly(coef, x, x_r)

print(f"Приближенное значение функции в точке x_r = {x_r}: y_r = {y_r}")