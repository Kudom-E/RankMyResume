import httpx
import pytest
import openai
import os
from src.get_embedding import get_embedding
import numpy as np


def test_get_embedding_on_no_input(capfd):
    with pytest.raises(ValueError):
        get_embedding("")


def test_get_embedding_invalid_api_key(mocker):
    mock_res = mocker.Mock(spec=httpx.Response)
    mock_res.status_code = 401
    mock_res.headers = {"Content-Type": "application/json"}

    os.environ["OPENAI_API_KEY"] = "invalid_key"
    mock_error = openai.AuthenticationError(
        "Invalid API key",
        response=mock_res,
        body={"mock_request"}
    )

    mocker.patch("openai.embeddings.create", side_effect=mock_error)

    with pytest.raises(openai.AuthenticationError):
        get_embedding(["test"])


@pytest.fixture
def mock_openai_embeddings_create(mocker):
    mock_client = mocker.Mock()

    mock_client.embeddings.create.return_value = mocker.Mock(
        data=[
            mocker.Mock(embedding=[0.1, 0.2, 0.3]),
            mocker.Mock(embedding=[0.4, 0.5, 0.6])
        ]
    )

    mocker.patch("openai.OpenAI", return_value=mock_client)

    return mock_client


def test_get_embedding_valid_input(mock_openai_embeddings_create):
    mock_texts = ["text1", "text2"]

    embeddings = get_embedding(mock_texts)

    assert len(embeddings) == 2
    assert isinstance(embeddings[0], np.ndarray)
    assert embeddings[0].tolist() == [0.1, 0.2, 0.3]
    assert embeddings[1].tolist() == [0.4, 0.5, 0.6]


@pytest.fixture
def mock_openai_generic_exception(mocker):
    # Create a mock OpenAI client
    mock_client = mocker.Mock()

    # Mock the embeddings.create method to raise a generic exception
    mock_client.embeddings.create.side_effect = \
        RuntimeError("Unexpected error occurred")

    # Patch openai.OpenAI to return the mock client when instantiated
    mocker.patch("openai.OpenAI", return_value=mock_client)

    return mock_client


def test_get_embedding_generic_exception(mock_openai_generic_exception):
    mock_texts = ["text1", "text2"]

    # Expect the function to raise the generic exception
    with pytest.raises(RuntimeError, match="Unexpected error occurred"):
        get_embedding(mock_texts)
