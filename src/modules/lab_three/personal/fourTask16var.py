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
x_r = 6.480
x = np.array([5.10, 5.50, 5.90, 6.30, 6.70])  # Добавим больше точек для наглядности
y = np.array([20.0334, 21.4077, 22.7191, 23.9723, 25.1719])

# Вычисляем коэффициенты разделенных разностей
coef = divided_diff(x, y)

# Создаем массив точек для построения графика
x_vals = np.linspace(min(x), max(x), 100)
y_vals = [newton_poly(coef, x, xi) for xi in x_vals]

# Вычисляем значение интерполяционного многочлена в точке x_r
y_r = newton_poly(coef, x, x_r)

print(f"Приближенное значение функции в точке x_r = {x_r}: y_r = {y_r}")

# Построение графиков
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'bo', label='Исходные данные')
plt.plot(x_vals, y_vals, 'r-', label='Интерполяционный многочлен Ньютона')
plt.plot(x_r, y_r, 'go', label=f'Точка интерполяции (x_r = {x_r}, y_r = {y_r:.4f})')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Интерполяция многочленом Ньютона')
plt.legend()
plt.grid(True)
plt.show()