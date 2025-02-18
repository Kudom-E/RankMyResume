from src.get_resume_texts import get_resume_texts


def test_get_resume_texts_on_empty_list(capfd):
    resumes = []
    result = get_resume_texts(resumes)

    captured = capfd.readouterr()

    assert result == []
    assert "No resumes found" in captured.out


def test_get_resume_texts_on_mock_resumes(mocker):
    resume_pdfs = ["resume1.pdf", "resume2.pdf"]

    mock_resume_text = mocker.patch("src.get_resume_texts.extract_text", side_effect=lambda x: f"Extracted text from {x}")

    result = get_resume_texts(resume_pdfs)

    expected_result = ["Extracted text from resume1.pdf", "Extracted text from resume2.pdf"]

    assert result == expected_result
    mock_resume_text.assert_called()

