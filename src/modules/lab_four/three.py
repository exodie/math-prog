import numpy as np
import matplotlib.pyplot as plt

def three():
    # Данные
    x = np.array([1.1, 1.7, 2.4, 3.0, 3.7, 4.5, 5.1, 5.8])
    y = np.array([0.3, 0.6, 1.1, 1.7, 2.3, 3.0, 3.8, 4.6])

    # Логарифмируем данные
    ln_x = np.log(x)
    ln_y = np.log(y)

    # Количество точек
    n = len(x)

    # Вычисляем необходимые суммы
    sum_ln_x = np.sum(ln_x)
    sum_ln_y = np.sum(ln_y)
    sum_ln_x2 = np.sum(ln_x**2)
    sum_ln_x_ln_y = np.sum(ln_x * ln_y)

    # Вычисляем коэффициенты m и ln c
    m = (n * sum_ln_x_ln_y - sum_ln_x * sum_ln_y) / (n * sum_ln_x2 - sum_ln_x**2)
    ln_c = (sum_ln_y - m * sum_ln_x) / n

    # Восстанавливаем c
    c = np.exp(ln_c)

    print("Задание 3")
    print(f"Степенная функция: y = {c:.4f}x^{m:.4f}")

    # Построение графика
    x_plot = np.linspace(min(x), max(x), 500)
    y_plot = c * x_plot**m

    plt.scatter(x, y, color='blue', label='Экспериментальные точки')
    plt.plot(x_plot, y_plot, color='red', label=f'Аппроксимирующая степенная функция: y = {c:.4f}x^{m:.4f}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title('Аппроксимация степенной функцией методом наименьших квадратов')
    plt.grid(True)
    plt.show()