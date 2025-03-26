import numpy as np
import matplotlib.pyplot as plt

# 1. Метод половинного деления для уравнения 3x^3 - 2x^2 + 2x - 5 = 0
def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("Функция должна иметь разные знаки на концах отрезка")

    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2
        if f(c) == 0:
            break
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iter_count += 1

    return (a + b) / 2

# Уравнение 3x^3 - 2x^2 + 2x - 5 = 0
f1 = lambda x: 3*x**3 - 2*x**2 + 2*x - 5

# Уточнение корня на отрезке [1, 2]
root1 = bisection_method(f1, 1, 2)
print(f"Корень уравнения 3x^3 - 2x^2 + 2x - 5 = 0 на отрезке [1, 2]: {root1:.7f}")

# 2. Комбинированный метод хорд и касательных для уравнения y = 3x^2 - 18x - 8

# Метод Ньютона (касательных)
def newton_method(f, df, x0, tol=1e-6, max_iter=100):
    iter_count = 0
    while iter_count < max_iter:
        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
        iter_count += 1
    return x0

# Метод хорд
def chord_method(f, a, b, tol=1e-6, max_iter=100):
    iter_count = 0
    while iter_count < max_iter:
        x = a - f(a) * (b - a) / (f(b) - f(a))
        if abs(f(x)) < tol:
            return x
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
        iter_count += 1
    return x

# Уравнение y = 3x^2 - 18x - 8
f2 = lambda x: 3*x**2 - 18*x - 8
df2 = lambda x: 6*x - 18  # Производная для метода Ньютона

# Применяем метод Ньютона для большего корня
root2_newton = newton_method(f2, df2, 7)
print(f"Больший корень уравнения 3x^2 - 18x - 8 = 0 (метод Ньютона): {root2_newton:.7f}")

# Применяем метод хорд для меньшего корня
root2_chord = chord_method(f2, -1, 0)
print(f"Меньший корень уравнения 3x^2 - 18x - 8 = 0 (метод хорд): {root2_chord:.7f}")

# Визуализация функций
def plot_function(f, a, b, title):
    x_vals = np.linspace(a, b, 400)
    y_vals = f(x_vals)
    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label="f(x)")
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()

# Построение графиков
plot_function(f1, 0, 2, "График функции 3x^3 - 2x^2 + 2x - 5 = 0")
plot_function(f2, -1, 7, "График функции y = 3x^2 - 18x - 8")