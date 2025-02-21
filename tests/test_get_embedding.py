import pytest
import openai
from src.get_embedding import get_embedding


def test_get_embedding_on_no_input(capfd):
    result = get_embedding("")

    captured = capfd.readouterr()

    assert result is None
    assert "No text to  be embedded" in captured.out
