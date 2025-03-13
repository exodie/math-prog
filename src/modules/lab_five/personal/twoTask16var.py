import numpy as np
from scipy.interpolate import lagrange

# Заданные значения
x = np.array([0.2, 0.4, 0.5])
y = np.array([0.45, 0.63, 0.70])

# Интерполяция многочленом Лагранжа
poly_lagrange = lagrange(x, y)

# Нахождение первой и второй производных для Лагранжа
derivative_1_lagrange = np.polyder(poly_lagrange, 1)
derivative_2_lagrange = np.polyder(poly_lagrange, 2)

# Вычисление производных в точке x_2 = 0.4
x_2 = 0.4
y_prime_x2_lagrange = np.polyval(derivative_1_lagrange, x_2)
y_double_prime_x2_lagrange = np.polyval(derivative_2_lagrange, x_2)

print(f"Лагранж: y'(x_2) = {y_prime_x2_lagrange}")
print(f"Лагранж: y''(x_2) = {y_double_prime_x2_lagrange}")


# Интерполяция многочленом Ньютона
def divided_diff(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    coef[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])

    return coef[0, :]


def newton_poly(coef, x_data, x):
    n = len(coef) - 1
    p = coef[n]
    for k in range(1, n + 1):
        p = coef[n - k] + (x - x_data[n - k]) * p
    return p


coef = divided_diff(x, y)
poly_newton = np.poly1d([coef[2], coef[1] - coef[2] * (x[0] + x[1]), coef[0] - coef[1] * x[0] + coef[2] * x[0] * x[1]])

# Нахождение первой и второй производных для Ньютона
derivative_1_newton = np.polyder(poly_newton, 1)
derivative_2_newton = np.polyder(poly_newton, 2)

# Вычисление производных в точке x_2 = 0.4
y_prime_x2_newton = np.polyval(derivative_1_newton, x_2)
y_double_prime_x2_newton = np.polyval(derivative_2_newton, x_2)

print(f"Ньютон: y'(x_2) = {y_prime_x2_newton}")
print(f"Ньютон: y''(x_2) = {y_double_prime_x2_newton}")