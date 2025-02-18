from unittest.mock import patch
import pytest
import os
import tempfile
from main import get_files


# @pytest.fixture
# def mock_os_scandir():
#     with  patch('os.scandir') as mock_scandir:


def test_directory_input(monkeypatch, mocker):
    mock_input = "Documents/Resumes"
    monkeypatch.setattr("builtins.input", lambda _: mock_input)
    monkeypatch.setattr("os.chdir", lambda _: None)

    # Creating mock DirEntry objects
    mock_files = [
        mocker.Mock(spec=os.DirEntry, name="resume1.pdf"),
        mocker.Mock(spec=os.DirEntry, name="job_description.html"),
        mocker.Mock(spec=os.DirEntry, name="desktop.ini")  # Should be ignored
    ]

    # Setting attributes and methods for each mock file
    mock_files[0].name = "resume1.pdf"
    mock_files[0].is_file.return_value = True

    mock_files[1].name = "job_description.html"
    mock_files[1].is_file.return_value = True

    mock_files[2].name = "desktop.ini"
    mock_files[2].is_file.return_value = True  # Even if it's a file, assume it's filtered out

    mocker.patch("os.scandir", return_value=mock_files)

    result = get_files()

    expected_files = ["resume1.pdf", "job_description.html"]

    assert isinstance(result, list)
    assert result == expected_files
