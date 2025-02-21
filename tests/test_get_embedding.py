import httpx
import pytest
import openai
import os
from src.get_embedding import get_embedding


def test_get_embedding_on_no_input(capfd):
    result = get_embedding("")

    captured = capfd.readouterr()

    assert result is None
    assert "No text to  be embedded" in captured.out


def test_get_embedding_invalid_api_key(capfd, mocker):
    mock_res = mocker.Mock(spec=httpx.Response)
    mock_res.status_code = 401
    mock_res.headers = {"Content-Type": "application/json"}

    os.environ["OPENAI_API_KEY"] = "invalid_key"
    mock_error = openai.AuthenticationError(
        "Invalid API key",
        response=mock_res,
        body={"mock_request"}
    )

    captured = capfd.readouterr()

    mocker.patch("openai.embeddings.create", side_effect=mock_error)

    with pytest.raises(openai.AuthenticationError):
        get_embedding(["test"])




