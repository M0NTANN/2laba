


def karatsuba_multiply(A, B):


    # Определение длины чисел и середины
    n = max(len(str(A)), len(str(B)))

    if n<2:
        return A * B
    k = (n + 1) // 2  # Округление вверх для k

    # Деление чисел на две части
    A0 = A % (10 ** k)  # Младшая часть A
    A1 = A // (10 ** k)  # Старшая часть A
    B0 = B % (10 ** k)  # Младшая часть B
    B1 = B // (10 ** k)  # Старшая часть B

    # Знаки для промежуточных вычислений
    sA = 1 if (A0 - A1) >= 0 else -1
    sB = 1 if (B0 - B1) >= 0 else -1

    # Рекурсивные вызовы для C0, C1 и C2
    C0 = karatsuba_multiply(A0, B0)
    C1 = karatsuba_multiply(A1, B1)
    C2 = karatsuba_multiply(abs(A0 - A1), abs(B0 - B1))

    # Результат согласно формуле
    result = C0 + ((C0 + C1 - sA * sB * C2) * (10 ** k)) + (C1 * (10 ** (2 * k)))
    return result

# Пример использования
x = 1234
y = 5678
result = karatsuba_multiply(x, y)
print("Результат умножения:", result)



