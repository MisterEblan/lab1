import pytest
from main import f

def test_zero_division(bad_xs: list[float]) -> None:
    """Тест на поднятие исключение о делении на ноль"""
    for x in bad_xs:
        with pytest.raises(ZeroDivisionError):
            print(f"x={x}, f(x)={f(x)}")
