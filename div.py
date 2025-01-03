import datetime
import gmpy2
from sympy import Integer

def newton_method_division(num1, num2, iterations=10):
    # Начальное приближение для 1/y
    inv_y = 1 / num2

    # Итерации Ньютоновского метода
    for _ in range(iterations):
        inv_y = inv_y * (2 - num2 * inv_y)

    # Результат деления
    return num1 * inv_y


def div(num1, num2):
    # Базовый случай
    if num1 < num2:
        return (0, num1)  # Если x меньше y, то деление дает 0, а остаток равен x

    # Рекурсивный случай
    quotient, remainder = div(num1 - num2, num2)
    return (quotient + 1, remainder)

# Пример использования
num1 = '10'
num2 = '3'
start = datetime.datetime.now()
r1, r2 = div(int(num1), int(num2))
end = datetime.datetime.now() - start
print(f"Результат деления : {r1},{r2}  Время выполнения: {end}")




start = datetime.datetime.now()
rr = newton_method_division(int(num1), int(num2))
end = datetime.datetime.now() - start
print(f"\nРезультат деления метод ньютон : {rr}  Время выполнения: {end}")


start = datetime.datetime.now()
res = gmpy2.div(int(num1), int(num2))
end = datetime.datetime.now() - start
print(f"\nРезультат деления gmpy2: {res}  Время выполнения: {end}")




start = datetime.datetime.now()
result = Integer(int(num1)) / Integer(int(num2))
end = datetime.datetime.now() - start
print(f"\nРезультат деления sympy: {res}  Время выполнения: {end}")
