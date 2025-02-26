def calculate_errors(a, b, delta_a, delta_b_rel):
    delta_b_abs = delta_b_rel * abs(b)

    # Для a + b
    sum_abs = delta_a + delta_b_abs
    sum_rel = sum_abs / abs(a + b) if (a + b) != 0 else float('inf')

    # Для a - b
    diff_abs = delta_a + delta_b_abs
    diff_val = a - b
    diff_rel = diff_abs / abs(diff_val) if diff_val != 0 else float('inf')

    # Для a * b
    prod_abs = abs(a) * delta_b_abs + abs(b) * delta_a
    prod_rel = (delta_a / abs(a)) + delta_b_rel if a != 0 else float('inf')

    # Для a / b
    if b == 0:
        div_abs = div_rel = float('inf')
    else:
        div_abs = (delta_a + abs(a) * delta_b_rel) / abs(b)
        div_rel = (delta_a / abs(a)) + delta_b_rel if a != 0 else float('inf')

    return {
        'a+b': (sum_abs, sum_rel),
        'a-b': (diff_abs, diff_rel),
        'a*b': (prod_abs, prod_rel),
        'a/b': (div_abs, div_rel)
    }

def two():
    # Пример использования
    print("Задание 2:")
    a = 10.0
    b = 20.0
    delta_a = 0.5
    delta_b_rel = 0.05  # 5%

    errors = calculate_errors(a, b, delta_a, delta_b_rel)

    for op in errors:
        abs_err, rel_err = errors[op]
        print(f"{op}:")
        print(f"  Абсолютная погрешность: {abs_err:.4f}")
        print(f"  Относительная погрешность: {rel_err:.2%}\n")

    # Пример с близкими значениями a и b
    a_close = 5.1
    b_close = 5.0
    errors_close = calculate_errors(a_close, b_close, 0.1, 0.01)

    print("Случай a ≈ b (a - b):")
    abs_err, rel_err = errors_close['a-b']
    print(f"  Абсолютная погрешность: {abs_err:.4f}")
    print(f"  Относительная погрешность: {rel_err:.2%}")
    print()
