def split_number(num, n):
    """
    Разбивает число на n частей.
    """
    parts = []
    base = 10 ** (len(str(num)) // n)
    for _ in range(n):
        parts.append(num % base)
        num //= base
    return parts[::-1]

def toom_cook_multiplication(x, y):
    """
    Реализация умножения чисел по методу Toom-Cook-3.
    """
    # Базовый случай: если числа маленькие, выполняем обычное умножение
    if x < 10 or y < 10:
        return x * y

    # Шаг 1: Разбиваем числа на 3 части
    n = max(len(str(x)), len(str(y)))
    k = (n + 2) // 3  # Размер одной части
    base = 10 ** k

    a = [x // (base ** i) % base for i in range(3)]
    b = [y // (base ** i) % base for i in range(3)]

    # Шаг 2: Вычисляем значения полиномов в точках (интерполяция)
    p0 = a[0]               # P(0)
    p1 = a[0] + a[1] + a[2] # P(1)
    p_1 = a[0] - a[1] + a[2] # P(-1)
    p2 = a[0] + 2 * a[1] + 4 * a[2] # P(2)
    p_inf = a[2]            # P(inf)

    q0 = b[0]               # Q(0)
    q1 = b[0] + b[1] + b[2] # Q(1)
    q_1 = b[0] - b[1] + b[2] # Q(-1)
    q2 = b[0] + 2 * b[1] + 4 * b[2] # Q(2)
    q_inf = b[2]            # Q(inf)

    # Шаг 3: Рекурсивно перемножаем полученные значения
    r0 = toom_cook_multiplication(p0, q0)
    r1 = toom_cook_multiplication(p1, q1)
    r_1 = toom_cook_multiplication(p_1, q_1)
    r2 = toom_cook_multiplication(a[0] + 2*int([1]) + 4*int(a[2]), b[0] + 2*int(b[1]) + 4*int(b[2]))
    r_inf = toom_cook_multiplication(p_inf, q_inf)

    # Шаг 4: Решаем систему для восстановления результата
    r_middle = (r1 - r_1) // 2
    r_bottom = (r1 - r0) - r_middle
    r_top = r_inf
    r_quadratic = (r2 - r1 - 4 * r_middle) // 6

    # Шаг 5: Собираем результат с учётом базиса
    result = r0 + r_bottom * base + r_middle * (base ** 2) + r_quadratic * (base ** 3) + r_top * (base ** 4)

    return result

# Тест
x = 1234
y = 5678
result = toom_cook_multiplication(x, y)
print(f"{x} * {y} = {result}")
print("Проверка встроенным умножением:", x * y)
