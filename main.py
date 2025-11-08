from math import sin, cos

calculate = lambda x: (
    ((sin(x) + cos(2 * x)** 2) / sin(2 * x))
    if abs(sin(2*x)) > 1e-2
    else "Знаменатель близок к нулю!"
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
        print(f"f={result:.6}")
    else:
        print(result)

run = lambda: print_result((get_input()))

run()
