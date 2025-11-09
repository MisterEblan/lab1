from math import sin, sqrt

# Значение аргумента, при котором функция не определена
BAD_X = 3

calculate = lambda x: (
    (sin(x) * sqrt( (x+3) / (x-3) ))
    if x != BAD_X or (x + 3) / (x - 3) < 0
    else f"Функция не определена в точке {x}"
)
"""Функция для вычисления значений"""

get_input = lambda: float(input("Ввод: >>> "))

def print_result(x: float) -> None:
    """Вывод результата вычислений

    Args:
        x: значение аргумента.

    Returns:
        только создаёт побочный эффект в виде вывода на экран
        результата вычислений или сообщения об ошибке.
    """
    result = calculate(x)

    print(f"x={x}")

    if isinstance(result, float):
        print(f"f={result:.3}")
    else:
        print(result)

run = lambda: print_result((get_input()))

run()
