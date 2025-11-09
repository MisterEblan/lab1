from main import main
from unittest.mock import MagicMock, patch

@patch("builtins.print")
@patch("builtins.input", return_value="5")
def test_normal(
    mock_input: MagicMock,
    mock_print: MagicMock
) -> None:
    main()

    called_args = [str(c) for c in mock_print.call_args_list]
    for arg in called_args:
        if "-1.92" in arg:
            assert True
            return

    assert False, "Ожидалось, что будет вычислено значение функции в точке 5"
