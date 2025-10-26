from main import f

eps = 1e-5

def test_normal(xs: dict[float, float]) -> None:
    """Тест на вычисление функции в точках
    с точностью до 5 знаков после запятой"""
    for x, y in xs.items():
        assert y - eps < (result := f(x)) < y + eps, \
            f"Ожидалось, что f({x}) будет равно {y}, " + \
            f"получили {result}"
