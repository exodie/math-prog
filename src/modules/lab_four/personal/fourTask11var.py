import numpy as np
import matplotlib.pyplot as plt

# Данные
x = np.array([0.2, 1.2, 3.2, 6.2, 8.2, 10.2])
y = np.array([3.6, 4.9, 5.8, 8.7, 9.4, 11.8])

# Количество точек
n = len(x)

# Аппроксимация многочленом первой степени
A1 = np.vstack([x, np.ones(n)]).T
a1, b1 = np.linalg.lstsq(A1, y, rcond=None)[0]
y1 = a1 * x + b1

# Аппроксимация многочленом второй степени
A2 = np.vstack([x**2, x, np.ones(n)]).T
a2, b2, c2 = np.linalg.lstsq(A2, y, rcond=None)[0]
y2 = a2 * x**2 + b2 * x + c2

# Вычисление средних квадратических уклонений
delta1 = np.sqrt(np.mean((y - y1)**2))
delta2 = np.sqrt(np.mean((y - y2)**2))

print(f"Линейная функция: y = {a1:.4f}x + {b1:.4f}")
print(f"Среднее квадратическое уклонение для линейной функции: δ_1 = {delta1:.4f}")
print(f"Квадратичная функция: y = {a2:.4f}x^2 + {b2:.4f}x + {c2:.4f}")
print(f"Среднее квадратическое уклонение для квадратичной функции: δ_2 = {delta2:.4f}")

# Построение графиков
x_plot = np.linspace(min(x), max(x), 500)
y1_plot = a1 * x_plot + b1
y2_plot = a2 * x_plot**2 + b2 * x_plot + c2

plt.scatter(x, y, color='blue', label='Экспериментальные точки')
plt.plot(x_plot, y1_plot, color='red', label=f'Линейная аппроксимация: y = {a1:.4f}x + {b1:.4f}')
plt.plot(x_plot, y2_plot, color='green', label=f'Квадратичная аппроксимация: y = {a2:.4f}x^2 + {b2:.4f}x + {c2:.4f}')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Аппроксимация методом наименьших квадратов')
plt.grid(True)
plt.show()