def split_into_blocks(number, base):

    #Разбивает число на блоки в заданной системе счисления.

    blocks = []
    block_size = len(str(base)) - 1
    while number:
        blocks.append(int(number[-block_size:]))
        number = number[:-block_size]
    return blocks

def subtract_large_numbers(A_str, B_str, base):

    #Вычитание больших чисел, представленных в обычной форме.
    A = A_str
    B = B_str
    # Проверка, какое число больше, для корректного определения знака
    is_negative = False
    if int(A) < int(B):
        # Если A меньше B, инвертируем их для вычитания
        A, B = B, A
        is_negative = True


    # Разбиваем числа на блоки
    A = split_into_blocks(A, base)
    B = split_into_blocks(B, base)

    # Убедимся, что длины массивов одинаковы, добавив ведущие нули в B
    n = len(A)
    B += [0] * (n - len(B))



    C = [0] * n  # Результат вычитания
    borrow = 0   # Переменная для хранения заема

    for i in range(n):
        # Вычитание с учетом заема
        c = A[i] - B[i] - borrow

        if c < 0:
            c += base  # Занимаем из старшего разряда
            borrow = 1
        else:
            borrow = 0

        C[i] = c

    # Удаляем ведущие нули из результата
    while len(C) > 1 and C[-1] == 0:
        C.pop()

    # Формируем строковое представление результата
    result = ''.join(f'{block:0{len(str(base)) - 1}d}' for block in C[::-1]).lstrip('0')

    if is_negative:
        result = '-' + result

    return result if result else '0'



    # Результат: C = A - B
C = subtract_large_numbers(str(55667), str(23778), 10000)
print("Результат вычитания:", C)
