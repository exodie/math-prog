def sum_with_errors(numbers, errors=None):
    """
    Вычисляет сумму чисел и их погрешности.
    :param numbers: список чисел
    :param errors: список погрешностей (если None, погрешности вычисляются автоматически)
    :return: сумма, абсолютная погрешность суммы
    """
    if errors is None:
        # Если погрешности не заданы, считаем их равными половине единицы последнего разряда
        errors = [0.5 * 10 ** (-len(str(num).split('.')[1])) if '.' in str(num) else 0.5 for num in numbers]

    total_sum = sum(numbers)
    total_error = sum(errors)

    return total_sum, total_error

def five():
    print("Задание 5:")
    # а) 0,145 + 321 + 78,2
    numbers_a = [0.145, 321, 78.2]
    sum_a, error_a = sum_with_errors(numbers_a)
    print(f"а) Сумма: {sum_a}, Погрешность: {error_a}")

    # б) 0,301 + 193,1 + 11,58
    numbers_b = [0.301, 193.1, 11.58]
    sum_b, error_b = sum_with_errors(numbers_b)
    print(f"б) Сумма: {sum_b}, Погрешность: {error_b}")

    # в) 398,5 – 72,28 + 0,34567
    numbers_c = [398.5, -72.28, 0.34567]
    sum_c, error_c = sum_with_errors(numbers_c)
    print(f"в) Сумма: {sum_c}, Погрешность: {error_c}")

    # г) 203,5 + 0,567 + 17,12
    numbers_d = [203.5, 0.567, 17.12]
    sum_d, error_d = sum_with_errors(numbers_d)
    print(f"г) Сумма: {sum_d}, Погрешность: {error_d}")

    # д) x1 + x2 - x3
    x1, delta_x1 = 197.6, 0.2
    x2, delta_x2 = 23.44, 0.22
    x3, delta_x3 = 201.55, 0.17

    numbers_e = [x1, x2, -x3]
    errors_e = [delta_x1, delta_x2, delta_x3]
    sum_e, error_e = sum_with_errors(numbers_e, errors_e)
    print(f"д) Сумма: {sum_e}, Погрешность: {error_e}")
    print()