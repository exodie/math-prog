import numpy as np
import matplotlib.pyplot as plt

x_values = np.array([0, 3, 4, 6])
y_values = np.array([25, -8, -15, -23])

def lagrange_interpolation(x, x_values, y_values):
    n = len(x_values)
    result = 0.0
    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if j != i:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term
    return result

x_interp = np.linspace(min(x_values), max(x_values), 100)
y_interp = [lagrange_interpolation(x, x_values, y_values) for x in x_interp]

y_exact = [lagrange_interpolation(x, x_values, y_values) for x in x_values]

for x, y in zip(x_values, y_exact):
    print(f"f({x}) = {y}")

plt.scatter(x_values, y_values, color='red', label='Исходные данные')
plt.plot(x_interp, y_interp, label='Многочлен Лагранжа', color='blue')
plt.title('Интерполяция Лагранжа')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
