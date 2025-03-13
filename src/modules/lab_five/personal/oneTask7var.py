import numpy as np
import matplotlib.pyplot as plt

# Функция
def y(x):
    if np.any(x <= 1):
        return np.nan  # Возвращаем NaN для недопустимых значений
    return np.log(np.log(np.log(x**2)))

# Точная первая производная
def y_prime(x):
    if np.any(x <= 1):
        return np.nan  # Возвращаем NaN для недопустимых значений
    return 2 / (x * np.log(x**2) * np.log(np.log(x**2)))

# Точная вторая производная
def y_double_prime(x):
    if np.any(x <= 1):
        return np.nan  # Возвращаем NaN для недопустимых значений
    term1 = -2 / (x**2 * np.log(x**2) * np.log(np.log(x**2)))
    term2 = -4 / (x**2 * np.log(x**2)**2 * np.log(np.log(x**2)))
    term3 = -4 / (x**2 * np.log(x**2) * np.log(np.log(x**2))**2)
    return term1 + term2 + term3

# Разностные производные
def right_diff(y, x, h):
    return (y(x + h) - y(x)) / h

def left_diff(y, x, h):
    return (y(x) - y(x - h)) / h

def central_diff(y, x, h):
    return (y(x + h) - y(x - h)) / (2 * h)

def second_diff(y, x, h):
    return (y(x + h) - 2 * y(x) + y(x - h)) / h**2

# Параметры
h1 = 2
h2 = 0.5
x_values = np.linspace(1.01, 10, 100)  # Начинаем с 1.01, чтобы избежать проблем с логарифмами

# Вычисление производных
x_h1 = np.arange(1.01, 10 + h1, h1)
x_h2 = np.arange(1.01, 10 + h2, h2)

# Для h1
y_prime_right_h1 = [right_diff(y, x, h1) for x in x_h1[:-1]]
y_prime_left_h1 = [left_diff(y, x, h1) for x in x_h1[1:]]
y_prime_central_h1 = [central_diff(y, x, h1) for x in x_h1[1:-1]]
y_double_prime_h1 = [second_diff(y, x, h1) for x in x_h1[1:-1]]

# Для h2
y_prime_right_h2 = [right_diff(y, x, h2) for x in x_h2[:-1]]
y_prime_left_h2 = [left_diff(y, x, h2) for x in x_h2[1:]]
y_prime_central_h2 = [central_diff(y, x, h2) for x in x_h2[1:-1]]
y_double_prime_h2 = [second_diff(y, x, h2) for x in x_h2[1:-1]]

# Точные значения
y_prime_exact = y_prime(x_values)
y_double_prime_exact = y_double_prime(x_values)

# Построение графиков
plt.figure(figsize=(14, 10))

# Первая производная
plt.subplot(2, 1, 1)
plt.plot(x_values, y_prime_exact, label='Точная первая производная', color='black')
plt.plot(x_h1[:-1], y_prime_right_h1, 'o-', label=f'Правая разностная (h={h1})')
plt.plot(x_h1[1:], y_prime_left_h1, 's-', label=f'Левая разностная (h={h1})')
plt.plot(x_h1[1:-1], y_prime_central_h1, 'd-', label=f'Центральная разностная (h={h1})')
plt.plot(x_h2[:-1], y_prime_right_h2, 'o-', label=f'Правая разностная (h={h2})')
plt.plot(x_h2[1:], y_prime_left_h2, 's-', label=f'Левая разностная (h={h2})')
plt.plot(x_h2[1:-1], y_prime_central_h2, 'd-', label=f'Центральная разностная (h={h2})')
plt.xlabel('x')
plt.ylabel("y'")
plt.legend()
plt.title('Первая производная')

# Вторая производная
plt.subplot(2, 1, 2)
plt.plot(x_values, y_double_prime_exact, label='Точная вторая производная', color='black')
plt.plot(x_h1[1:-1], y_double_prime_h1, 'o-', label=f'Вторая разностная (h={h1})')
plt.plot(x_h2[1:-1], y_double_prime_h2, 's-', label=f'Вторая разностная (h={h2})')
plt.xlabel('x')
plt.ylabel("y''")
plt.legend()
plt.title('Вторая производная')

plt.tight_layout()
plt.show()

