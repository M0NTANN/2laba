import datetime
import gmpy2
from sympy import Integer


def karatsubaMultiply(num1, num2):

    # Определение длины чисел и середины
    n = max(len(str(num1)), len(str(num2)))

    # Если n > 1, тогда результат не может быть получен обычным умножением
    if n == 1:
        return num1 * num2

    k = n  // 2  # Округление вверх для k



    # Деление чисел на две части
    A0 = num1 % (10 ** k)  # Младшая часть num1
    A1 = num1 // (10 ** k)  # Старшая часть num1
    B0 = num2 % (10 ** k)  # Младшая часть num2
    B1 = num2 // (10 ** k)  # Старшая часть num2

    # Знаки для промежуточных вычислений
    sA = 1 if (A0 - A1) >= 0 else -1
    sB = 1 if (B0 - B1) >= 0 else -1

    # Рекурсивные вызовы для C0, C1 и C2
    C0 = karatsubaMultiply(A0, B0)
    C1 = karatsubaMultiply(A1, B1)
    C2 = karatsubaMultiply(abs(A0 - A1), abs(B0 - B1))

    # Результат согласно формуле
    result = C0 + ((C0 + C1 - sA * sB * C2) * (10 ** k)) + (C1 * (10 ** (2 * k)))


    return result

# Пример использования
num_1 = 123433123433123433123433123433123433123433123433123433123433123433123433123433123433123433123433
num_2 = 567833567833567833567833567833567833567833567833567833567833567833567833567833567833567833567833567833567833567833567833567833567833567833567833
start = datetime.datetime.now()
result = karatsubaMultiply(int(num_1), int(num_2))
end = datetime.datetime.now() - start
print(f"Результат умножения: {result} Время выполнения: {end}")


start = datetime.datetime.now()
res = gmpy2.mul(int(num_1) , int(num_2))
end = datetime.datetime.now() - start
print(f"\nРезультат умножения gmpy2: {res}  Время выполнения: {end}")




start = datetime.datetime.now()
result = Integer(num_1) * Integer(num_2)
end = datetime.datetime.now() - start
print(f"\nРезультат умножения sympy: {res}  Время выполнения: {end}")


