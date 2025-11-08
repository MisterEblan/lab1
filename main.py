from math import sin, cos

eps: float = 1e-2

def f(x: float) -> float:
    """
    Вычисляет значение выражения
    $$ \\frac{(\\sin(x) + \\cos (2x) )^2}{\\sin(2x)} $$

    Область определения:
        Вся вещественная прямая, кроме точек
        $\\frac{\\pi n}{2}, n \\in \\mathbb{N}$.

    Args:
        x: значение аргумента.

    Returns:
        Вычисленное значение.

    Raises:
        ZeroDivisionError: если подать значение не из области определения.
    """

    if abs(denominator := sin(2 * x)) < eps:
        raise ZeroDivisionError("Знаменатель близок к нулю!")

    enumerator = ( sin(x) + cos(x * 2) )**2

    f_x = enumerator / denominator

    return f_x

def main():
    x = float(input("Ввод >> "))

    result = f(x)

    print(f"x={x}")
    print(f"f={result:.6}")

if __name__ == "__main__":
    main()
