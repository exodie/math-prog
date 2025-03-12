import numpy as np
import matplotlib.pyplot as plt

def one():
    # Данные
    x = np.array([1.0, 1.5, 2.5, 3.0, 4.5, 5.1, 6.2])
    y = np.array([67, 101, 168, 202, 301, 334, 404])

    # Количество точек
    n = len(x)

    # Вычисляем необходимые суммы
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x2 = np.sum(x**2)
    sum_xy = np.sum(x * y)

    # Вычисляем коэффициенты a и b
    a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
    b = (sum_y - a * sum_x) / n

    print("Задание 1")
    print(f"Линейная зависимость: y = {a:.2f}x + {b:.2f}")
    print()

    # Построение графика
    plt.scatter(x, y, color='blue', label='Экспериментальные точки')
    plt.plot(x, a * x + b, color='red', label=f'Аппроксимирующая прямая: y = {a:.2f}x + {b:.2f}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title('Линейная аппроксимация методом наименьших квадратов')
    plt.grid(True)
    plt.show()