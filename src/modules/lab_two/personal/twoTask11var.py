import numpy as np
import matplotlib.pyplot as plt

x_values = np.array([-2, -1, 0, 1, 2])
y_values = np.array([5, 0, 1, 0, 5])

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

# Находим коэффициенты полинома с помощью numpy.polyfit
coefficients = np.polyfit(x_values, y_values, len(x_values) - 1)

# Формируем строку для полинома
polynomial_terms = []
for i, coeff in enumerate(coefficients):
    power = len(coefficients) - 1 - i
    if power == 0:
        polynomial_terms.append(f"{coeff:.2f}")
    elif power == 1:
        polynomial_terms.append(f"{coeff:.2f}*x")
    else:
        polynomial_terms.append(f"{coeff:.2f}*x^{power}")

# Упрощаем строку, убирая лишние нули и добавляя знаки
polynomial_formula = " + ".join(term.replace("+-", "- ") for term in polynomial_terms).replace(" 1.00*", " ").replace(" -", " - ")

x_interp = np.linspace(min(x_values), max(x_values), 100)
y_interp = [lagrange_interpolation(x, x_values, y_values) for x in x_interp]

y_exact = [lagrange_interpolation(x, x_values, y_values) for x in x_values]

for x, y in zip(x_values, y_exact):
    print(f"f({x}) = {y}")

print("Формула полинома Лагранжа:")
print(polynomial_formula)

plt.scatter(x_values, y_values, color='red', label='Исходные данные')
plt.plot(x_interp, y_interp, label='Многочлен Лагранжа', color='blue')
plt.title('Интерполяция Лагранжа')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
