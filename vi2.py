from datetime import datetime

import numpy
from mpmath import mp
import numpy as np
import random


def main():
    while True:
        print("\n\n\nВыберите действие: \n"
              "1 Сложение \n"
              "2 Вычитание \n"
              "3 Умножение \n"
              "4 Выход")
        choiceU = int(input(">>>"))

        if choiceU == 1:
            n = int(input("Введите размер массива: "))
            x = [random.randint(0, 9) for _ in range(n)]
            y = [random.randint(0, 9) for _ in range(n)]
            print(f"{x}")
            print(f"{y}")
            start = datetime.now()
            result = add(x, y)
            end = datetime.now() - start
            print(f"\nРезультат сложения : {result}  \n       Время выполнения: {end}\n\n")

            mp.dps = 100
            x = mp.mpf(int(''.join(map(str, x))))
            y = mp.mpf(int(''.join(map(str, y))))
            start = datetime.now()
            result = x + y
            end = datetime.now() - start
            print(f"Результат numpy сложение векторов: {result}  \n     Время выполнения: {end}\n\n")



        if choiceU == 2:
            n = int(input("Введите размер массива: "))
            x = [random.randint(0, 9) for _ in range(n)]
            y = [random.randint(0, 9) for _ in range(n)]
            print(f"{x}")
            print(f"{y}")
            start = datetime.now()
            result = sub(x, y)
            end = datetime.now() - start
            print(f"Результат вычитания : {result}  \n       Время выполнения: {end}\n\n")

            mp.dps = 100
            x = mp.mpf(int(''.join(map(str, x))))
            y = mp.mpf(int(''.join(map(str, y))))
            start = datetime.now()
            result = x - y
            end = datetime.now() - start
            print(f"\nРезультат поэлементное вычитание векторов: {int(result)}  \n Время выполнения: {end}\n\n")


        if choiceU == 3:
            n = int(input("Введите размер массива: "))
            x = [random.randint(0, 9) for _ in range(n)]
            y = [random.randint(0, 9) for _ in range(n)]
            print(f"{x}")
            print(f"{y}")
            start = datetime.now()
            result = karatsubaMul(x, y)
            end = datetime.now() - start
            print(f"Результат умножения: {result} \n        Время выполнения: {end}\n\n")

            mp.dps = 100
            x = mp.mpf(int(''.join(map(str,x))))
            y = mp.mpf(int(''.join(map(str,y))))
            start = datetime.now()
            res = x * y
            end = datetime.now() - start
            print(f"\nРезультат вычитания gmpy2: {res}  \n      Время выполнения: {end}")


def sub(x, y):

    result = ''
    borrow = 0
    for i in range(len(x) - 1, -1, -1):
        diff = x[i] - y[i] - borrow
        if diff < 0:
            diff += 10  # Заимствование (borrow)
            borrow = 1
        else:
            borrow = 0
        result += str(diff)

    # Разворачиваем список результата и преобразуем в число
    result = int(''.join(map(str, result[::-1])))

    if borrow == 1:
        result = (10 ** len(x) - result) * (-1)

    # Перемножаем на признак отрицательного числа
    result = str(int(result))

    return result

def elemSubVek(x, y):


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

    return result_str

def add(x, y):

    result = ''  # Список для хранения результата поразрядного сложения
    carry = 0  # Переменная для хранения переноса

    # Складываем числа справа налево
    for i in range(len(x) - 1, -1, -1):
        sum = x[i] + y[i] + carry  # Сумма текущих разрядов и переноса
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




def karatsubaMul(x, y):

    # Определение длины чисел и середины
    n = len(x)

    # Если n > 1, тогда результат не может быть получен обычным умножением
    if n == 1:
        return x[0] * y[0]

    k = n // 2  # Округление вверх для k

    # Деление чисел на две части
    A0 = int(''.join(map(str, [x[i] for i in range(n - k,n,1)])))  # Младшая часть x
    A1 = int(''.join(map(str, [x[i] for i in range(0,n - k,1)])))  # Старшая часть x
    B0 = int(''.join(map(str, [y[i] for i in range(n - k,n,1)])))  # Младшая часть y
    B1 = int(''.join(map(str, [y[i] for i in range(0,n - k,1)])))   # Старшая часть y

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
    C0 = karatsubaMul([int(digit) for digit in str(A0)], [int(digit) for digit in str(B0)])
    C1 = karatsubaMul([int(digit) for digit in str(A1)], [int(digit) for digit in str(B1)])
    C2 = karatsubaMul([int(digit) for digit in str(abs(A0 - A1))], [int(digit) for digit in str(abs(B0 - B1))])

    # Результат согласно формуле
    result = C0 + ((C0 + C1 - sA * sB * C2) * (10 ** k)) + (C1 * (10 ** (2 * k)))

    return result

if __name__ == "__main__":    main()