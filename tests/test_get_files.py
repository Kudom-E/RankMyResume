import os
from src.get_files import get_files


def test_get_files_no_input(monkeypatch, capfd):
    mock_input = ""
    monkeypatch.setattr("builtins.input", lambda _: mock_input)

    get_files(max_retries=3)
    captured = capfd.readouterr()

    assert "❌ No directory entered. Please enter a valid path." in captured.out


def test_get_files_validate_input(monkeypatch, mocker, capfd):
    mock_input = mocker.patch("builtins.input", side_effect=["invalid/path", "valid/path"])
    mock_exists = mocker.patch("os.path.exists", side_effect=[False, True])
    monkeypatch.setattr("os.chdir", lambda _: None)

    get_files()
    captured = capfd.readouterr()

    assert "❌ Invalid directory. Please check the path and try again." in captured.out
    assert f"✅ Directory set to: {os.path.abspath(os.path.expanduser('~/valid/path'))}" in captured.out

    assert mock_input.call_count == 2
    assert mock_exists.call_count == 2


def test_get_files_on_mock_files(monkeypatch, mocker):
    mock_input = "Documents/Resumes"
    monkeypatch.setattr("builtins.input", lambda _: mock_input)
    monkeypatch.setattr("os.chdir", lambda _: None)

    # Creating mock DirEntry objects
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

    mocker.patch("os.scandir", return_value=mock_files)

    resume_pdf, job_html = get_files()

    expected_files = (["resume1.pdf", "resume2.pdf"], ["job_description.html"])

    assert isinstance(resume_pdf, list)
    assert isinstance(job_html, list)
    assert resume_pdf, job_html == expected_files

# def test_get_files_no_files():
