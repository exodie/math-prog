"""С каким числом верных знаков следует взять значение аргумента x, чтобы получить значения указанных функций с точностью до 10^-6.
а) y = x^3sin(x), x = sqrt(2)
б) y = xlnx, x = p
в) y = e^xcosx, x = sqrt(3)
г) y = x^2lgx, x = корень третьей степениз из двух
"""


import math
from decimal import Decimal, getcontext

"""getcontext(): Эта функция возвращает текущий контекст вычислений для чисел с плавающей запятой, 
которые представлены классом Decimal. Контекст включает в себя настройки, такие как точность, режим округления и другие параметры.
.prec = 6: Эта часть кода устанавливает количество значащих цифр (точность) для всех последующих операций с числами 
типа Decimal на 6. Это означает, что все вычисления, которые вы будете выполнять с числами Decimal, будут округлены до 6 значащих цифр.
"""

def eight():

    # Устанавливаем точность до 10^-6
    getcontext().prec = 7  # Устанавливаем достаточную точность для вычислений

    def calculate_y1(x):
        return Decimal(x)**3 * Decimal(math.sin(float(x)))

    def calculate_y2(x):
        return Decimal(x) * Decimal(math.log(float(x)))

    def calculate_y3(x):
        return Decimal(math.exp(float(x))) * Decimal(math.cos(float(x)))

    def calculate_y4(x):
        return Decimal(x)**2 * Decimal(math.log10(float(x)))

    # Значения x
    x1 = Decimal(2).sqrt()  # sqrt(2)
    x2 = Decimal(math.e)  # p (число e)
    x3 = Decimal(3).sqrt()  # sqrt(3)
    x4 = Decimal(2)**(Decimal(1)/Decimal(3))  # корень третьей степени из 2

    # Вычисляем значения функций
    y1 = calculate_y1(x1)
    y2 = calculate_y2(x2)

    getcontext().prec = 6

    y3 = calculate_y3(x3)
    y4 = calculate_y4(x4)

    # Выводим результаты
    print("Задание 8")
    print(f"y = x^3 * sin(x), x = sqrt(2). Точность 7 знаков: {y1}")
    print(f"y = x * ln(x), x = e. . Точность 7 знаков {y2}")
    print(f"y = e^x * cos(x), x = sqrt(3). Точность 6 знаков {y3}")
    print(f"y = x^2 * log10(x), x = 3sqrt(3). Точность 6 знаков {y4}")
