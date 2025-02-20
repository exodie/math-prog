def absolute_error(a, delta):
    return abs(a) * (delta / 100)


def three():
    data = [
        (13267, 0.1),
        (2.32, 0.7),
        (35.72, 1),
        (0.896, 10),
        (232.44, 1)
    ]

    print("Задание 3:")
    for a, delta in data:
        abs_error = absolute_error(a, delta)
        print(f"Для a = {a} и δ = {delta}%: Абсолютная погрешность = {abs_error:.5f}")
    print()
