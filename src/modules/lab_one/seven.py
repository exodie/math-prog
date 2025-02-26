"""
Вычислить значение z=ln⁡(10.3+ √(4.4)), считая верными все знаки приближенных чисел x=10.3 и y=4.4.
"""

import math


def seven():
    x = 10.3
    y = 4.4

    koren = round(math.sqrt(y), 1)

    summa = round(koren + x, 1)

    z = math.log(summa)
    print("Задание 7:")
    print(f"Значение z = {z:.2f}")
