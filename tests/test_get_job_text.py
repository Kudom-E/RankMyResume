from unittest.mock import mock_open
from src.get_job_text import get_job_text


def test_get_job_text_on_no_job(capfd):
    result = get_job_text("")

    captured = capfd.readouterr()

    assert result is None
    assert "No job description found" in captured.out


def test_get_job_text_on_mock_job(mocker):
    # Mocking 'open' to return specific file content
    mocker.patch(
        "builtins.open", new_callable=mock_open,
        read_data="<html><main>Job Description</main></html>"
    )

    result = get_job_text("fake_job.html")

    assert result == "Job Description"
