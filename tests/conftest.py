import pytest
from math import pi, sqrt

@pytest.fixture
def bad_xs() -> list[float]:
    """Точки, для которых функция не определена"""
    return [
        pi,
        3 * pi / 2,
        2 * pi,
        -pi,
        -3 * pi / 2,
        -2 * pi
    ]

@pytest.fixture
def xs() -> dict[float, float]:
    """Тестовые точки"""
    return {
        pi / 3: (2 / sqrt(3)) - 1,
        pi / 4: 1 / 2,
        -pi / 3: -1 - (2 / sqrt(3)),
        -pi / 4: - 1 / 2
    }
