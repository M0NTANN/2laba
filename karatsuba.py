import datetime
import gmpy2
import numpy as np
from sympy import Integer


def karatsubaMul(x, y):

    # Определение длины чисел и середины
    n = max(len(str(x)), len(str(y)))

    # Если n > 1, тогда результат не может быть получен обычным умножением
    if n == 1:
        return x * y

    k = n  // 2  # Округление вверх для k



    # Деление чисел на две части
    A0 = x % (10 ** k)  # Младшая часть num1
    A1 = x // (10 ** k)  # Старшая часть num1
    B0 = y % (10 ** k)  # Младшая часть num2
    B1 = y // (10 ** k)  # Старшая часть num2

    # Знаки для промежуточных вычислений
    if (A0 - A1) >= 0:
        sA = 1
    else:
        sA = -1
    if (B0 - B1) >= 0:
        sB = 1
    else:
        sB = -1

    # Рекурсивные вызовы для C0, C1 и C2
    C0 = karatsubaMul(A0, B0)
    C1 = karatsubaMul(A1, B1)
    C2 = karatsubaMul(abs(A0 - A1), abs(B0 - B1))

    # Результат согласно формуле
    result = C0 + ((C0 + C1 - sA * sB * C2) * (10 ** k)) + (C1 * (10 ** (2 * k)))


    return result

# Пример использования
num1 = '970'
num2 = '884'
start = datetime.datetime.now()
result = karatsubaMul(int(num1), int(num2))
end = datetime.datetime.now() - start
print(f"Результат умножения: {result} \n- Время выполнения: {end}\n\n")



start = datetime.datetime.now()
res = gmpy2.mul(int(num1), int(num2))
end = datetime.datetime.now() - start
print(f"\nРезультат вычитания gmpy2: {res}   \n- Время выполнения: {end}")




start = datetime.datetime.now()
result = Integer(int(num1)) * Integer(int(num2))
end = datetime.datetime.now() - start
print(f"\nРезультат вычитания sympy: {res}  \n- Время выполнения: {end}")






