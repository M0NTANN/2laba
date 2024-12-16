def prefix_sum_addition(num1, num2):
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
    if carry:
        result.append(carry)

    # Разворачиваем список результата и преобразуем в число
    return int(''.join(map(str, result[::-1])))

# Пример использования
num1 = 22690
num2 = 2289
result = prefix_sum_addition(num1, num2)
print(f"Результат сложения : {result}")
