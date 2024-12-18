import datetime

import gmpy2
from sympy import Integer


def sub(A_str, B_str):
    start = datetime.datetime.now()

    is_negative = False
    if int(A_str) < int(B_str):
        # Если A меньше B, инвертируем их для вычитания
        A_str, B_str = B_str, A_str
        is_negative = True

    # Преобразуем строки в массивы цифр
    A = [int(digit) for digit in A_str]
    B = [int(digit) for digit in B_str]

    # Убедимся, что числа одинаковой длины. Если нужно, добавим ведущие нули в меньшую длину
    n = max(len(A), len(B))
    A = [0] * (n - len(A)) + A
    B = [0] * (n - len(B)) + B

    # Массив для результата вычитания
    result = []
    borrow = 0

    # Перебор цифр с конца (с младших разрядов)
    for i in range(n - 1, -1, -1):
        diff = A[i] - B[i] - borrow
        if diff < 0:
            diff += 10  # Заимствование (borrow)
            borrow = 1
        else:
            borrow = 0
        result.append(diff)

    # Результат хранится в обратном порядке, так что переворачиваем его
    result.reverse()

    # Убираем ведущие нули
    while len(result) > 1 and result[0] == 0:
        result.pop(0)

    if is_negative:
        result.insert(0, '-')

    end = datetime.datetime.now() - start

    result = int(''.join(map(str, result[::1])))

    return end, result



num1 = '2223423423423423234234232324324234269022234234'
num2 = '49228234234232342342342342342342344232349'
end, result = sub(num1, num2)
print(f"Результат вычитания : {result}  Время выполнения: {end}")


start = datetime.datetime.now()
res = gmpy2.sub(int(num1), int(num2))
end = datetime.datetime.now() - start
print(f"\nРезультат вычитания gmpy2: {res}  Время выполнения: {end}")




start = datetime.datetime.now()
result = Integer(int(num1)) - Integer(int(num2))
end = datetime.datetime.now() - start
print(f"\nРезультат вычитания sympy: {res}  Время выполнения: {end}")