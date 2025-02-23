from unittest.mock import mock_open

import pytest

from src.get_job_text import get_job_text


def test_on_no_job():
    with pytest.raises(ValueError):
        get_job_text("")


def test_on_mock_job(mocker):
    # Mocking 'open' to return specific file content
    mocker.patch(
        "builtins.open", new_callable=mock_open,
        read_data="<html><main>Job Description</main></html>"
    )

    result = get_job_text("fake_job.html")

    assert result == "Job Description"


def test_on_multi_lines(mocker):
    # Mocking 'open' to return specific file content
    mocker.patch(
        "builtins.open", new_callable=mock_open,
        read_data="<html><main>\n\n Job  \n Description \n\n</main></html>"
    )

    result = get_job_text("fake_job.html")

    assert result == "Job Description"
