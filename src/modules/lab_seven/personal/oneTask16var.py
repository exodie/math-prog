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


# Уравнение x^5 - 7x + 1 = 0
f1 = lambda x: x ** 5 - 7 * x + 1

# Уточнение корня на отрезке [-2, -1.5]
root1 = bisection_method(f1, -2, -1.5)
print(f"Корень уравнения x^5 - 7x = -1 на отрезке [-2, -1.5]: {root1:.7f}")


# Метод Ньютона
def newton_method(f, df, x0, tol=1e-6, max_iter=100):
    iter_count = 0
    while iter_count < max_iter:
        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
        iter_count += 1
    return x0

# Уравнение x^3 - 3x - 1 = 0
f2 = lambda x: x**3 - 3*x - 1
df2 = lambda x: 3*x**2 - 3

# Уточнение корня на отрезке [1.5, 2]
root2 = newton_method(f2, df2, 1.5)
print(f"Корень уравнения x^3 - 3x = 1 на отрезке [1.5, 2]: {root2:.7f}")

# Модифицированный метод Ньютона
def modified_newton_method(f, df, x0, tol=1e-6, max_iter=100):
    iter_count = 0
    df_x0 = df(x0)  # Фиксируем производную в начальной точке
    while iter_count < max_iter:
        x1 = x0 - f(x0) / df_x0
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
        iter_count += 1
    return x0

# Уточнение корня на отрезке [1.5, 2]
root3 = modified_newton_method(f1, lambda x: 5*x**4 - 7, 1.5)
print(f"Корень уравнения x^5 - 7x = -1 на отрезке [1.5, 2]: {root3:.7f}")

# Метод простых итераций
def simple_iteration_method(phi, x0, tol=1e-6, max_iter=100):
    iter_count = 0
    while iter_count < max_iter:
        x1 = phi(x0)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
        iter_count += 1
    return x0

# Уравнение x^2 - 12 = 0
phi = lambda x: np.sqrt(12) if x < 0 else -np.sqrt(12)  # Итерационная функция

# Уточнение корня на отрезке [-4, -3]
root4 = simple_iteration_method(phi, -3.5)
print(f"Корень уравнения x^2 - 12 = 0 на отрезке [-4, -3]: {root4:.7f}")

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

# Уравнение x^3 - 7x^2 + x + 3 = 0
f3 = lambda x: x**3 - 7*x**2 + x + 3
plot_function(f3, -1, 8, "График функции x^3 - 7x^2 + x + 3 = 0")

# Уравнение y = 7x^2 - 28x - 3
f4 = lambda x: 7*x**2 - 28*x - 3
plot_function(f4, -2, 6, "График функции y = 7x^2 - 28x - 3")