from main import main
from unittest.mock import MagicMock, patch

@patch("builtins.print")
@patch("builtins.input", return_value="1.04719")
def test_normal(
    mock_input: MagicMock,
    mock_print: MagicMock
) -> None:
    main()

    called_args = [c for c in mock_print.call_args_list]
    assert ("f=" in arg for arg in called_args)
    assert ("x=1.04719" in arg for arg in called_args)
