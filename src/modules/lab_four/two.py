import numpy as np
import matplotlib.pyplot as plt

def two():
    # Данные
    x = np.array([2.0, 2.2, 2.4, 2.6, 2.8, 3.0])
    y = np.array([0.30, 0.34, 0.38, 0.42, 0.44, 0.48])

    # Количество точек
    n = len(x)

    # Вычисляем необходимые суммы
    sum_x = np.sum(x)
    sum_x2 = np.sum(x**2)
    sum_x3 = np.sum(x**3)
    sum_x4 = np.sum(x**4)
    sum_y = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_x2y = np.sum(x**2 * y)

    # Составляем систему уравнений
    A = np.array([
        [n, sum_x, sum_x2],
        [sum_x, sum_x2, sum_x3],
        [sum_x2, sum_x3, sum_x4]
    ])

    B = np.array([sum_y, sum_xy, sum_x2y])

    # Решаем систему уравнений
    a, b, c = np.linalg.solve(A, B)

    print("Задание 2")
    print(f"Квадратный трехчлен: y = {a:.4f}x^2 + {b:.4f}x + {c:.4f}")
    print()

    # Построение графика
    x_plot = np.linspace(min(x), max(x), 500)
    y_plot = a * x_plot**2 + b * x_plot + c

    plt.scatter(x, y, color='blue', label='Экспериментальные точки')
    plt.plot(x_plot, y_plot, color='red', label=f'Аппроксимирующая парабола: y = {a:.4f}x^2 + {b:.4f}x + {c:.4f}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title('Аппроксимация квадратным трехчленом методом наименьших квадратов')
    plt.grid(True)
    plt.show()