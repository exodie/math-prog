import numpy as np
import matplotlib.pyplot as plt


def divided_diff(x, y):
    """
    Вычисляет коэффициенты разделенных разностей для интерполяционного многочлена Ньютона.
    """
    n = len(y)
    coef = np.zeros([n, n])
    coef[:, 0] = y  # Первый столбец — значения y

    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])

    return coef[0, :]  # Возвращаем первую строку коэффициентов


def newton_poly(coef, x_data, x):
    """
    Вычисляет значение интерполяционного многочлена Ньютона в точке x.
    """
    n = len(coef) - 1
    p = coef[n]
    for k in range(1, n + 1):
        p = coef[n - k] + (x - x_data[n - k]) * p
    return p


# Данные из варианта 16
x_r = 8.4
x = np.array([-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([-203, -147, -96, -53, -31, -10, 2, 10, 15, 14, 12, 9, 7, 7, 9, 18, 26, 44, 70, 102])

# Вычисляем коэффициенты разделенных разностей
coef = divided_diff(x, y)

# Вычисляем значение интерполяционного многочлена в точке x_r
y_r = newton_poly(coef, x, x_r)

print(f"Приближенное значение функции в точке x_r = {x_r}: y_r = {y_r}")

# Построение интерполяционной кривой
x_plot = np.linspace(min(x), max(x), 500)
y_plot = [newton_poly(coef, x, xi) for xi in x_plot]

plt.plot(x, y, 'o', label='Узлы интерполяции')
plt.plot(x_plot, y_plot, label='Интерполяционная кривая')
plt.axvline(x=x_r, color='r', linestyle='--', label=f'x_r = {x_r}')
plt.axhline(y=y_r, color='g', linestyle='--', label=f'y_r = {y_r:.2f}')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Интерполяция функции методом Ньютона')
plt.grid(True)
plt.show() 