import datetime
import gmpy2
from sympy import Integer


def sub(num1, num2):

    # Старт работы программы
    start = datetime.datetime.now()

    # Проверяем не больше ли второе число
    is_negative = False
    if int(num1) < int(num2):
        # Если num1 меньше num2, инвертируем их для вычитания
        num1, num2 = num2, num1
        is_negative = True

    # Преобразуем строки в массивы цифр
    num1 = [int(digit) for digit in num1]
    num2 = [int(digit) for digit in num2]

    # Убедимся, что числа одинаковой длины. Если нужно, добавим ведущие нули в меньшую длину
    n = max(len(num1), len(num2))
    num1 = [0] * (n - len(num1)) + num1
    num2 = [0] * (n - len(num2)) + num2

    # Массив для результата вычитания
    result = []
    borrow = 0

    # Перебор цифр с конца (с младших разрядов)
    for i in range(n - 1, -1, -1):
        diff = num1[i] - num2[i] - borrow
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

    # Если второе число было больше первого ставим "-"
    if is_negative:
        result.insert(0, '-')

    # Конец работы программы
    end = datetime.datetime.now() - start

    # Разворачиваем список результата и преобразуем в число
    result = int(''.join(map(str, result[::1])))

    return end, result



num1 = '2223423423423423234234232324324234269022234234222342342342342323423423232432423426902223423422234234234234232342342323243242342690222342342223423423423423234234232324324234269022234234'
num2 = '492282342342323423423423423423423442323494922823423423234234234234234234234423234949228234234232342342342342342342344232349'
end, result = sub(num1, num2)
print(f"Результат вычитания : {result} \n- Время выполнения: {end}")


start = datetime.datetime.now()
res = gmpy2.sub(int(num1), int(num2))
end = datetime.datetime.now() - start
print(f"\nРезультат вычитания gmpy2: {res}   \n- Время выполнения: {end}")




start = datetime.datetime.now()
result = Integer(int(num1)) - Integer(int(num2))
end = datetime.datetime.now() - start
print(f"\nРезультат вычитания sympy: {res}  \n- Время выполнения: {end}")