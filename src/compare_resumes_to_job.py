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
