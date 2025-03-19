import numpy as np
import matplotlib.pyplot as plt

# Определение функции и её производных
def y(x):
    return x

def y_prime(x):
    return 1

def y_double_prime(x):
    return 0

# Вычисление разностных производных
def forward_diff(y, x, h):
    return (y(x + h) - y(x)) / h

def backward_diff(y, x, h):
    return (y(x) - y(x - h)) / h

def central_diff(y, x, h):
    return (y(x + h) - y(x - h)) / (2 * h)

def second_diff(y, x, h):
    return (y(x + h) - 2 * y(x) + y(x - h)) / h**2

# Параметры
h1 = 0.2
h2 = 0.05
x_values = np.arange(0, 1 + h2, h2)

# Вычисление производных
forward_diff_h1 = [forward_diff(y, x, h1) for x in x_values]
backward_diff_h1 = [backward_diff(y, x, h1) for x in x_values]
central_diff_h1 = [central_diff(y, x, h1) for x in x_values]
second_diff_h1 = [second_diff(y, x, h1) for x in x_values]

forward_diff_h2 = [forward_diff(y, x, h2) for x in x_values]
backward_diff_h2 = [backward_diff(y, x, h2) for x in x_values]
central_diff_h2 = [central_diff(y, x, h2) for x in x_values]
second_diff_h2 = [second_diff(y, x, h2) for x in x_values]

# Точные значения производных
exact_prime = [y_prime(x) for x in x_values]
exact_double_prime = [y_double_prime(x) for x in x_values]

# Вывод значений в консоль
print("x values:", x_values)
print("Forward difference (h1):", forward_diff_h1)
print("Backward difference (h1):", backward_diff_h1)
print("Central difference (h1):", central_diff_h1)
print("Second difference (h1):", second_diff_h1)
print("Forward difference (h2):", forward_diff_h2)
print("Backward difference (h2):", backward_diff_h2)
print("Central difference (h2):", central_diff_h2)
print("Second difference (h2):", second_diff_h2)
print("Exact first derivative:", exact_prime)
print("Exact second derivative:", exact_double_prime)

# Визуализация
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(x_values, forward_diff_h1, label='Forward h1')
plt.plot(x_values, forward_diff_h2, label='Forward h2')
plt.plot(x_values, exact_prime, label='Exact')
plt.title('Forward Difference')
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(x_values, backward_diff_h1, label='Backward h1')
plt.plot(x_values, backward_diff_h2, label='Backward h2')
plt.plot(x_values, exact_prime, label='Exact')
plt.title('Backward Difference')
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(x_values, central_diff_h1, label='Central h1')
plt.plot(x_values, central_diff_h2, label='Central h2')
plt.plot(x_values, exact_prime, label='Exact')
plt.title('Central Difference')
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(x_values, second_diff_h1, label='Second h1')
plt.plot(x_values, second_diff_h2, label='Second h2')
plt.plot(x_values, exact_double_prime, label='Exact')
plt.title('Second Difference')
plt.legend()

plt.tight_layout()
plt.show()