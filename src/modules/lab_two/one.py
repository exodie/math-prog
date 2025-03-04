import numpy as np

x_values = np.array([4, 9, 16, 25])
y_values = np.sqrt(x_values)

x_target = 11

if x_target < x_values[0] or x_target > x_values[-1]:
    raise ValueError("Точка вне диапазона известных значений.")

lower_index = np.searchsorted(x_values, x_target) - 1
upper_index = lower_index + 1

x_lower = x_values[lower_index]
y_lower = y_values[lower_index]
x_upper = x_values[upper_index]
y_upper = y_values[upper_index]

# Линейная интерполяция
y_target = y_lower + (y_upper - y_lower) * (x_target - x_lower) / (x_upper - x_lower)

# Оценка погрешности
true_value = np.sqrt(x_target)
error = abs(true_value - y_target)

print(f"Значение функции в точке {x_target}: {y_target}")
print(f"Истинное значение функции: {true_value}")
print(f"Погрешность: {error}")
