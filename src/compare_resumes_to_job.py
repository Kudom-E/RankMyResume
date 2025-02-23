import numpy as np


def compare_resumes_to_job(
        resume_embeddings, job_embedding, resume_list_names):
    if not resume_embeddings and \
            job_embedding and \
            resume_list_names:
        raise ValueError("Missing values")
    elif resume_embeddings == [] and \
            job_embedding == [] and \
            resume_list_names == []:
        raise ValueError("No values")

    # make sure the embedding lengths match the job description
    for embedding in resume_embeddings:
        if len(embedding) != len(job_embedding):
            raise ValueError(
                "An Embedding received is not matching the required length"
            )

    # make sure the magnitude from any embedding doesn't end up as zero
    for embedding in resume_embeddings + [job_embedding]:
        if np.linalg.norm(embedding) == 0:
            raise ZeroDivisionError(
                "Cannot calculate cosine similarity with zero-length vectors"
            )

    scores = {
        resume_list_names[i]: round(
            float(np.dot(
                resume_embeddings[i], job_embedding
            ) /
                  (np.linalg.norm(resume_embeddings[i]) *
                   np.linalg.norm(job_embedding))) * 100, 2
        )
        for i in range(len(resume_list_names))
    }

    return scores
