import math


def calculate_volume(h, S1, S2):
    """Вычисляет объем V."""
    return (1 / 3) * h * (S1 + S2 + math.sqrt(S1 * S2))


def calculate_absolute_error(h, S1, S2, delta_h, delta_S1, delta_S2):
    """Вычисляет абсолютную погрешность объема."""
    dV_dh = (1 / 3) * (S1 + S2 + math.sqrt(S1 * S2))
    dV_dS1 = (1 / 3) * h * (1 + S2 / (2 * math.sqrt(S1 * S2)))
    dV_dS2 = (1 / 3) * h * (1 + S1 / (2 * math.sqrt(S1 * S2)))

    delta_V = abs(dV_dh) * delta_h + abs(dV_dS1) * delta_S1 + abs(dV_dS2) * delta_S2
    return delta_V

data = [
    {"h": 21.7, "delta_h": 0.02, "S1": 9.272, "delta_S1": 0.001, "S2": 11.01, "delta_S2": 0.005},
    {"h": 3.45, "delta_h": 0.01, "S1": 17.654, "delta_S1": 0.0005, "S2": 2.19, "delta_S2": 0.02},
    {"h": 0.956, "delta_h": 0.004, "S1": 5.322, "delta_S1": 0.0005, "S2": 1.315, "delta_S2": 0.0004},
]

for i, case in enumerate(data, start=1):
    h = case["h"]
    S1 = case["S1"]
    S2 = case["S2"]
    delta_h = case["delta_h"]
    delta_S1 = case["delta_S1"]
    delta_S2 = case["delta_S2"]

    V = calculate_volume(h, S1, S2)
    delta_V = calculate_absolute_error(h, S1, S2, delta_h, delta_S1, delta_S2)

    print(f"Случай {i}:")
    print(f"  Объем V = {V:.6f} см³")
    print(f"  Абсолютная погрешность ΔV = {delta_V:.6f} см³")
    print()