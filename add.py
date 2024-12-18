import datetime
import gmpy2
from sympy import Integer

def add(num1, num2):

    # Старт работы программы
    start = datetime.datetime.now()

    # Преобразуем числа в строки для работы поразрядно
    num1, num2 = str(num1), str(num2)

    # Дополняем числа нулями слева, чтобы их длины совпадали
    max_len = max(len(num1), len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)

    result = []  # Список для хранения результата поразрядного сложения
    carry = 0  # Переменная для хранения переноса

    # Складываем числа справа налево
    for i in range(max_len - 1, -1, -1):
        sum = int(num1[i]) + int(num2[i]) + carry  # Сумма текущих разрядов и переноса
        result.append(sum % 10)  # Записываем младший разряд
        carry = sum // 10  # Вычисляем перенос

    # Если после сложения остался перенос, добавляем его
    if carry == 1:
        result.append(carry)

    # Разворачиваем список результата и преобразуем в число
    result = int(''.join(map(str, result[::-1])))

    # Конец работы программы
    end = datetime.datetime.now() - start

    return end, result

# Пример использования
num1 = '492249224922492249224922492249224922492249224922492249224922492249224922492249224922492249224922492249224922492249224922492249224922492249224922492249224922492249224922492249224922492249224922492249224922492249224922492249224922492249224922492249224922492249224922492249224922'
num2 = '1231231231123123123112312312311231231231123123123112312312311231231231123123123112312312311231231231123123123112312312311231231231123123123112312312311231231231123123123112312312311231231231123123123112312312311231231231'
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

