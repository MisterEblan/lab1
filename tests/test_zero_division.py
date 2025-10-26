import pytest
from main import main
from unittest.mock import MagicMock, patch

@patch("builtins.input", return_value="3.1415")
@patch("builtins.print")
def test_zero_division(
    mock_input: MagicMock,
    mock_print: MagicMock
) -> None:
    """Тест на поднятие исключение о делении на ноль"""
    with pytest.raises(ZeroDivisionError):
        main()
