import numpy as np
import pytest

from src.compare_resumes_to_job import compare_resumes_to_job


def test_on_no_input():
    with pytest.raises(ValueError):
        compare_resumes_to_job([], [], [])


def test_on_mock_embeddings():
    mock_resume_embeddings = [
        np.array([1, 2, 3]),
        np.array([4, 5, 6]),
        np.array([7, 8, 9])
    ]

    mock_job_embeddings = np.array([1, 1, 1])
    mock_resume_list_names = ["resume1", "resume2", "resume3"]

    expected_scores = {
        "resume1": 92.58,
        "resume2": 98.69,
        "resume3": 99.48
    }

    scores = compare_resumes_to_job(mock_resume_embeddings,
                                    mock_job_embeddings,
                                    mock_resume_list_names)

    assert scores == expected_scores


def test_on_different_length_embeddings():
    mock_resume_embeddings = [np.array([1, 2, 3])]
    mock_job_embedding = np.array([1, 1])
    mock_resume_list_names = ["resume1"]

    with pytest.raises(ValueError):
        compare_resumes_to_job(mock_resume_embeddings,
                               mock_job_embedding,
                               mock_resume_list_names)


def test_on_zero_length_vectors_in_embedding():
    mock_resume_embeddings = [np.array([0, 0, 0])]
    mock_job_embedding = np.array([1, 1, 1])
    mock_resume_list_names = ["resume1"]

    with pytest.raises(ZeroDivisionError):
        compare_resumes_to_job(mock_resume_embeddings,
                               mock_job_embedding,
                               mock_resume_list_names)
