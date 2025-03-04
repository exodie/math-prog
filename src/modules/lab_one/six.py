def six():
    a = 8.0
    delta_a = 0.02

    V = a**3

    delta_V = 3 * a**2 * delta_a

    relative_delta_V = delta_V / V

    print("Задание 6:")
    print(f"Объем куба: V = {V} см³")
    print(f"Абсолютная погрешность объема: ΔV = {delta_V} см³")
    print(f"Относительная погрешность объема: δV = {relative_delta_V}")
    print()