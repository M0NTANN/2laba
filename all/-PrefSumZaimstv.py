def subtract_large_numbers(A_str, B_str):

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

    return result



result = subtract_large_numbers(str(9912), str(4412))
print(f"Результат вычитания: {''.join(map(str, result))}")  # Выводим результат как строку
