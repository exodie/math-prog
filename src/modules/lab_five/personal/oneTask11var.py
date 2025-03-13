import numpy as np
import matplotlib.pyplot as plt

# Функция
def y(x):
    return np.sin(np.arcsin(x))

# Точная первая производная
def y_prime(x):
    with np.errstate(divide='ignore', invalid='ignore'):
        result = 1 / np.sqrt(1 - x**2)
        result[x == 1] = np.nan  # Обработка x = 1
    return result

# Точная вторая производная
def y_double_prime(x):
    with np.errstate(divide='ignore', invalid='ignore'):
        result = x / (1 - x**2)**(3/2)
        result[x == 1] = np.nan  # Обработка x = 1
    return result

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
h1 = 0.2
h2 = 0.05
x_values = np.linspace(0, 0.99, 100)  # Избегаем x = 1

# Вычисление производных
x_h1 = np.arange(0, 1, h1)
x_h2 = np.arange(0, 1, h2)

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