import math

def absolute_error(a, delta_a, l, delta_l, phi, delta_phi):
    # Вычисляем частные производные
    partial_a = math.log(phi)
    partial_l = math.sin(phi)
    partial_phi = (a / phi) + l * math.cos(phi)
    
    # Вычисляем абсолютную погрешность
    delta_y = abs(partial_a) * delta_a + abs(partial_l) * delta_l + abs(partial_phi) * delta_phi
    return delta_y

# Заданные значения
values = [
    (3.889, 0.001, 0.8454, 0.0002, 0.643, 0.0005),
    (145.5, 0.08, 28.6, 0.1, 0.1736, 0.00005),
    (27.3, 0.04, 0.93, 0.001, 1.73, 0.03)
]

# Вычисляем абсолютную погрешность для каждого набора значений
for i, (a, delta_a, l, delta_l, phi, delta_phi) in enumerate(values, start=1):
    error = absolute_error(a, delta_a, l, delta_l, phi, delta_phi)
    print(f"Абсолютная погрешность для набора {i}: {error}")