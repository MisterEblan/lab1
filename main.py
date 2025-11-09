from math import sin, sqrt

# Значение аргумента, при котором функция не определена
BAD_X = 3

def f(x: float) -> float:
    """
    Вычисляет значение выражения
    $$ \\sin (x) \\sqrt{ \\frac{x + 3}{x - 3} } $$

    Область определения:
        Вся вещественная прямая, кроме точки $x=3$.

    Args:
        x: значение аргумента.

    Returns:
        Вычисленное значение.

    Raises:
        ZeroDivisionError: если подать значение не из области определения.
    """

    if x == BAD_X:
        raise ZeroDivisionError(f"Функция не определена в точке {x}")

    f_x = sin(x) * sqrt( (x + 3) / (x - 3) )

    return f_x

def main():
    x = float(input("Ввод >> "))

    result = f(x)

    print(f"x={x}")
    print(f"f={result:.6}")

if __name__ == "__main__":
    main()
