import numpy as np
import matplotlib.pyplot as plt

# Метод половинного деления
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

# Уравнение x^3 - 5x^2 + 5x + 13 = 0
f1 = lambda x: x**3 - 5*x**2 + 5*x + 13

# Уточнение корня на отрезке [-2, -1]
root1 = bisection_method(f1, -2, -1)
print(f"Корень уравнения x^3 - 5x^2 + 5x + 13 = 0 на отрезке [-2, -1]: {root1:.7f}")

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

# Метод хорд (секущих)
def secant_method(f, a, b, tol=1e-6, max_iter=100):
    iter_count = 0
    while iter_count < max_iter:
        x = a - f(a) * (b - a) / (f(b) - f(a))
        if abs(x - a) < tol:
            return x
        a, b = b, x
        iter_count += 1
    return x

# Уравнение y = x^2 - 14x - 2.8
f2 = lambda x: x**2 - 14*x - 2.8
df2 = lambda x: 2*x - 14  # Производная для метода Ньютона

# Применяем метод Ньютона (касательных) для положительного корня
root2_newton = newton_method(f2, df2, 15)
print(f"Положительный корень уравнения x^2 - 14x - 2.8 = 0 (метод Ньютона): {root2_newton:.7f}")

# Применяем метод хорд для отрицательного корня
root2_secant = secant_method(f2, -2, 0)
print(f"Отрицательный корень уравнения x^2 - 14x - 2.8 = 0 (метод хорд): {root2_secant:.7f}")

# Функция для построения графика
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
plot_function(f1, -3, 6, "График функции x^3 - 5x^2 + 5x + 13 = 0")
plot_function(f2, -3, 15, "График функции y = x^2 - 14x - 2.8")