from datetime import datetime
from mpmath import mp
import numpy as np


def main():
    while True:
        print("\n\n\nВыберите действие: \n"
              "1 Сложение \n"
              "2 Вычитание \n"
              "3 Умножение \n"
              "4 Выход")
        choiceU = int(input(">>>"))

        if choiceU == 1:
            x = 101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010
            y = 2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222323232323
            start = datetime.now()
            result = add(x, y)
            end = datetime.now() - start
            print(f"Результат сложения : {result}  \n       Время выполнения: {end.microseconds}\n\n")

            start = datetime.now()
            result = elemAddVek(np.array(list(map(int, str(x)))), np.array(list(map(int, str(y)))))
            end = datetime.now() - start
            print(f"Результат поэлементного сложения векторов: {result}  \n     Время выполнения: {end.microseconds}\n\n")

            mp.dps = 100
            x = mp.mpf(str(x))
            y = mp.mpf(str(y))
            start = datetime.now()
            result = x + y
            end = datetime.now() - start
            print(f"Результат сложения библиотека mpmath: {result}  \n     Время выполнения: {end.microseconds}")


        if choiceU == 2:
            y = 23
            x = 32
            start = datetime.now()
            result = sub(x, y)
            end = datetime.now() - start
            print(f"Результат вычитания : {result}  \n       Время выполнения: {end.microseconds}\n\n")

            is_negative = 1
            if int(abs(x)) < int(abs(y)):
                # Если x меньше y, инвертируем их для вычитания
                x, y = y, x
                is_negative = is_negative * -1
            start = datetime.now()
            res2 = elemSubVek(np.array(list(map(int, str(x)))), np.array(list(map(int, str(y)))))
            end = datetime.now() - start
            print(f"\nРезультат поэлементное вычитание векторов: {int(res2) * is_negative}  Время выполнения: {end.microseconds}\n\n")

            mp.dps = 100
            x = mp.mpf(str(x))
            y = mp.mpf(str(y))
            start = datetime.now()
            result = x - y
            end = datetime.now() - start
            print(f"Результат вычитания библиотека mpmath: {result}  \n     Время выполнения: {end.microseconds}")


        if choiceU == 3:
            x = 1010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010
            y = 2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            start = datetime.now()
            result = karatsubaMul(int(x), int(y))
            end = datetime.now() - start
            print(f"Результат умножения: {result} \n    Время выполнения: {end.microseconds}\n\n")


            xarr = np.array([x])
            yarr = np.array([y])
            start = datetime.now()
            res = sum(a * b for a, b in zip(xarr, yarr))
            end = datetime.now() - start
            print(f"\nРезультат скалярного произведение: {res}  \n Время выполнения: {end.microseconds}\n\n")

            mp.dps = 100
            x = mp.mpf(str(x))
            y = mp.mpf(str(y))
            start = datetime.now()
            result = x * y
            end = datetime.now() - start
            print(f"Результат умножения библиотека mpmath: {result}  \n     Время выполнения: {end.microseconds}")


def sub(x, y):

    is_negative = 1

    # Проверяем не больше ли второе число
    if int(abs(x)) < int(abs(y)) :
        # Если x меньше y, инвертируем их для вычитания
        x, y = y, x
        is_negative = is_negative * -1

    x = str(abs(x))
    y = str(abs(y))

    # Преобразуем строки в массивы цифр
    x = [int(digit) for digit in x]
    y = [int(digit) for digit in y]

    # Убедимся, что числа одинаковой длины. Если нужно, добавим ведущие нули в меньшую длину
    n = max(len(x), len(y))
    x = [0] * (n - len(x)) + x
    y = [0] * (n - len(y)) + y

    # Массив для результата вычитания
    result = ''
    borrow = 0

    # Перебор цифр с конца (с младших разрядов)
    for i in range(n - 1, -1, -1):
        diff = x[i] - y[i] - borrow
        if diff < 0:
            diff += 10  # Заимствование (borrow)
            borrow = 1
        else:
            borrow = 0
        result += str(diff)


    # Разворачиваем список результата и преобразуем в число
    result = int(''.join(map(str, result[::-1])))

    # Перемножаем на признак отрицательного числа
    result = str(int(result) * is_negative)

    return result


def add(x, y):

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

def elemAddVek(x, y):
    # Выравниваем длины массивов, добавляем ведущие нули
    if len(x) < len(y):
        x = np.pad(x, (len(y) - len(x), 0), 'constant')
    elif len(y) < len(x):
        y = np.pad(y, (len(x) - len(y), 0), 'constant')
    # Поэлементное сложение
    result = x + y

    # Обработка переноса
    for i in range(len(result) - 1, 0, -1):
        if result[i] >= 10:
            result[i] -= 10
            result[i - 1] += 1

    # Если есть перенос на старший разряд
    if result[0] >= 10:
        result[0] -= 10
        result = np.insert(result, 0, 1)

    # Результат в правильном порядке
    return int(''.join(map(str, result[::1])))

def elemSubVek(x, y):
    # Проверим, нужно ли менять местами числа для правильного знака
    result_is_negative = False

    if len(x) < len(y) or (len(x) == len(y) and x.all() < y.all()):
        x, y = y, x  # Меняем местами, чтобы результат был положительным
        result_is_negative = True

    # Выравниваем длины массивов, добавляем ведущие нули
    if len(x) < len(y):
        x = np.pad(x, (len(y) - len(x), 0), 'constant')
    elif len(y) < len(x):
        y = np.pad(y, (len(x) - len(y), 0), 'constant')

    # Поэлементное вычитание с обработкой заимствования
    result = x - y
    for i in range(len(result) - 1, 0, -1):
        if result[i] < 0:
            result[i] += 10
            result[i - 1] -= 1

    # Удаляем ведущий ноль, если есть
    if result[0] == 0 and len(result) > 1:
        result = result[1:]

    # Преобразуем результат в строку
    result_str = ''.join(map(str, result))
    if result_is_negative:
        result_str = '-' + result_str

    return result_str


def karatsubaMul(x, y):

    # Определение длины чисел и середины
    n = max(len(str(x)), len(str(y)))

    # Если n > 1, тогда результат не может быть получен обычным умножением
    if n == 1:
        return x * y

    k = n  // 2  # Округление вверх для k

    # Деление чисел на две части
    A0 = x % (10 ** k)  # Младшая часть x
    A1 = x // (10 ** k)  # Старшая часть x
    B0 = y % (10 ** k)  # Младшая часть y
    B1 = y // (10 ** k)  # Старшая часть y

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

if __name__ == "__main__":
    main()





