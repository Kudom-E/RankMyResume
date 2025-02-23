import os
import pytest
from src.get_files import get_files


# must test
@pytest.fixture
def mock_files(mocker):
    mock_files = [
        mocker.Mock(spec=os.DirEntry, name="resume1.pdf"),
        mocker.Mock(spec=os.DirEntry, name="resume2.pdf"),
        mocker.Mock(spec=os.DirEntry, name="job_description.html"),
        mocker.Mock(spec=os.DirEntry, name="desktop.ini")  # Should be ignored
    ]

    mock_files[0].name = "resume1.pdf"
    mock_files[0].is_file.return_value = True

    mock_files[1].name = "resume2.pdf"
    mock_files[1].is_file.return_value = True

    mock_files[2].name = "job_description.html"
    mock_files[2].is_file.return_value = True

    mock_files[3].name = "desktop.ini"
    mock_files[3].is_file.return_value = True

    return mock_files


def test_no_input(mocker, capfd):
    mock_input = ""
    mocker.patch("builtins.input", lambda _: mock_input)

    try:
        get_files(max_retries=3)
    except IndexError:
        captured = capfd.readouterr()

    assert "❌ No directory entered. Please enter a valid path." in captured.out


def test_on_too_many_retries(mocker):
    mocker.patch("builtins.input", return_value="invalid/path")

    with pytest.raises(IndexError):
        get_files(max_retries=2)


def test_on_validating_input(mocker, capfd):
    mock_input = mocker.patch(
        "builtins.input", side_effect=["invalid/path", "valid/path"]
    )
    mock_exists = mocker.patch("os.path.exists", side_effect=[False, True])
    mocker.patch("os.chdir", lambda _: None)
    mock_scandir = mocker.patch("os.scandir", return_value=[])

    try:
        get_files(max_retries=2)
    except ValueError:
        captured = capfd.readouterr()

    assert "❌ Invalid directory. " \
           "Please check the path and try again." \
           in captured.out

    assert f"✅ Directory set to: " \
           f"{os.path.abspath(os.path.expanduser('~/valid/path'))}" \
           in captured.out

    assert mock_input.call_count == 2
    assert mock_exists.call_count == 2

    mock_scandir.assert_called_once()


def test_on_no_valid_files(mocker):
    mock_input = "Documents/Resumes"
    mocker.patch("builtins.input", lambda _: mock_input)
    mocker.patch("os.chdir", lambda _: None)
    mocker.patch("os.path.exists", side_effect=[True])

    # Creating mock DirEntry objects with no valid files
    mock_files = [
        mocker.Mock(spec=os.DirEntry,
                    name="desktop.ini"),
        mocker.Mock(spec=os.DirEntry,
                    name="other_file.txt"),
    ]

    mocker.patch("os.scandir", return_value=mock_files)

    with pytest.raises(ValueError):
        get_files(max_retries=1)


def test_on_mock_files(monkeypatch, mocker, mock_files):
    mock_input = "Documents/Resumes"
    mocker.patch("builtins.input", lambda _: mock_input)
    mocker.patch("os.chdir", lambda _: None)
    mocker.patch("os.path.exists", side_effect=[True])
    mocker.patch("os.scandir", return_value=mock_files)

    resume_pdf, job_html = get_files(max_retries=1)

    expected_files = (["resume1.pdf", "resume2.pdf"], ["job_description.html"])

    assert isinstance(resume_pdf, list)
    assert isinstance(job_html, list)
    assert resume_pdf, job_html == expected_files
