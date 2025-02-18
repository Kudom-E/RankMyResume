import os
from main import get_files, get_resume_texts


def test_get_files(monkeypatch, mocker):
    mock_input = "Documents/Resumes"
    monkeypatch.setattr("builtins.input", lambda _: mock_input)
    monkeypatch.setattr("os.chdir", lambda _: None)

    # Creating mock DirEntry objects
    mock_files = [
        mocker.Mock(spec=os.DirEntry, name="resume1.pdf"),
        mocker.Mock(spec=os.DirEntry, name="job_description.html"),
        mocker.Mock(spec=os.DirEntry, name="desktop.ini")  # Should be ignored
    ]

    mock_files[0].name = "resume1.pdf"
    mock_files[0].is_file.return_value = True

    mock_files[1].name = "job_description.html"
    mock_files[1].is_file.return_value = True

    mock_files[2].name = "desktop.ini"
    mock_files[2].is_file.return_value = True

    mocker.patch("os.scandir", return_value=mock_files)

    result = get_files()

    expected_files = ["resume1.pdf", "job_description.html"]

    assert isinstance(result, list)
    assert result == expected_files


def test_get_resume_texts_on_empty_list(capfd):
    resumes = []
    result = get_resume_texts(resumes)

    captured = capfd.readouterr()

    assert result == []
    assert "No resumes found" in captured.out


def test_get_resume_texts_on_mock_resumes(mocker):
    resumes = ["resume1.pdf", "resume2.pdf"]

    mock_resume_text = mocker.patch("main.extract_text", side_effect=lambda x: f"Extracted text from {x}")

    result = get_resume_texts(resumes)

    expected_result = ["Extracted text from resume1.pdf", "Extracted text from resume2.pdf"]

    assert result == expected_result
    mock_resume_text.assert_called()