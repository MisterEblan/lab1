from math import sin, cos

eps: float = 1e-3

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

    if abs(sin(2 * x)) < eps:
        raise ZeroDivisionError()

    return (sin(x) + cos(2 * x))**2 / (sin(2 * x))

if __name__ == "__main__":
    x = float(input("Ввод >>> "))
    print(f"x = {x}")

    f_x = f(x)
    print(f"f = {f_x:.6f}")
