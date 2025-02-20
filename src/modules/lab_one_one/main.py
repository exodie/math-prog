import math

def calculate_errors(numbers):
    results = []
    for x in numbers:
        # Округляем до трёх значащих цифр
        approx = float(format(x, '.3g'))
        # Вычисляем абсолютную погрешность
        absolute_error = abs(x - approx)
        # Вычисляем относительную погрешность (в процентах)
        relative_error = absolute_error / abs(x) * 100 if x != 0 else 0
        results.append((approx, absolute_error, relative_error))
    return results

# Исходные числа
numbers = [0.16152, 0.01204, 1.225]

# Расчёт погрешностей
errors = calculate_errors(numbers)

# Вывод результатов
for i in range(len(numbers)):
    print(f"Число {numbers[i]}:")
    print(f"Приближённое значение: {errors[i][0]}")
    print(f"Абсолютная погрешность: {errors[i][1]}")
    print(f"Относительная погрешность: {errors[i][2]:.3f}%\n")