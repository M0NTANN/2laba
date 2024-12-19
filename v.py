from datetime import datetime
import gmpy2



def sub(num1, num2):



    if num1 < 0 and num2 < 0:
        result = add(num1 * -1, num2 * -1)
        return result * -1

    num1 = str(num1)
    num2 = str(num2)

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
    result = ''
    borrow = 0

    # Перебор цифр с конца (с младших разрядов)
    for i in range(n - 1, -1, -1):
        diff = num1[i] - num2[i] - borrow
        if diff < 0:
            diff += 10  # Заимствование (borrow)
            borrow = 1
        else:
            borrow = 0
        result += str(diff)




    # Разворачиваем список результата и преобразуем в число
    result = int(''.join(map(str, result[::-1])))

    if is_negative:
        result = str(int(result) * -1)

    return result


def add(x, y):

    if x < 0 or y < 0:
        sub(x,y)

    # Преобразуем числа в строки для работы поразрядно
    x_str = str(x)
    y_str = str(y)

    # Дополняем числа нулями слева, чтобы их длины совпадали
    max_len = max(len(x_str), len(y_str))
    x_str = x_str.zfill(max_len)
    y_str = y_str.zfill(max_len)

    result = ''  # Список для хранения результата поразрядного сложения
    carry = 0  # Переменная для хранения переноса

    # Складываем числа справа налево
    for i in range(max_len - 1, -1, -1):
        sum = int(x_str[i]) + int(y_str[i]) + carry  # Сумма текущих разрядов и переноса
        result += str(sum % 10)  # Записываем младший разряд
        carry = sum // 10  # Вычисляем перенос

    # Если после сложения остался перенос, добавляем его
    if carry == 1:
        result += '1'

    # Разворачиваем список результата и преобразуем в число
    result = int(''.join(map(str, result[::-1])))



    return result

# Пример использования
x = -65
y = -35
start = datetime.now()
result = sub(x, y)
end = datetime.now() - start
print(f"Результат сложения : {result}  Время выполнения: {end.microseconds}")


start = datetime.now()
res2 = gmpy2.sub(x, y)
end = datetime.now() - start
print(f"\nРезультат сложения gmpy2: {res2}  Время выполнения: {end.microseconds}")



