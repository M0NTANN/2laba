import datetime
import gmpy2
from sympy import Integer

def add(num1, num2):
    start = datetime.datetime.now()
    # Преобразуем числа в строки для работы поразрядно
    str1, str2 = str(num1), str(num2)

    # Дополняем числа нулями слева, чтобы их длины совпадали
    max_len = max(len(str1), len(str2))
    str1 = str1.zfill(max_len)
    str2 = str2.zfill(max_len)

    result = []  # Список для хранения результата поразрядного сложения
    carry = 0  # Переменная для хранения переноса

    # Складываем числа справа налево
    for i in range(max_len - 1, -1, -1):
        digit_sum = int(str1[i]) + int(str2[i]) + carry  # Сумма текущих разрядов и переноса
        result.append(digit_sum % 10)  # Записываем младший разряд
        carry = digit_sum // 10  # Вычисляем перенос

    # Если после сложения остался перенос, добавляем его
    if carry == 1:
        result.append(carry)

    result = int(''.join(map(str, result[::-1])))
    end = datetime.datetime.now() - start
    # Разворачиваем список результата и преобразуем в число
    return end, result

# Пример использования
num1 = '4922'
num2 = '4922'
end, result = add(int(num1), int(num2))
print(f"Результат сложения : {result}  Время выполнения: {end}")


start = datetime.datetime.now()
#res2 = gmpy2.mpz(num1) + gmpy2.mpz(num2)
res2 = gmpy2.add(int(num1), int(num2))
#res2 = gmpy2.add(gmpy2.mpz(num1),gmpy2.mpz(num2))
end = datetime.datetime.now() - start
print(f"\nРезультат сложения gmpy2: {res2}  Время выполнения: {end}")





start = datetime.datetime.now()
result = Integer(num1) + Integer(num2)
end = datetime.datetime.now() - start
print(f"\nРезультат сложения sympy: {result}  Время выполнения: {end}")

