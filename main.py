from src.get_embedding import get_embedding
from src.get_files import get_files
from src.get_job_text import get_job_text
from src.get_resume_texts import get_resume_texts
# push to test branch before any commit
if __name__ == "__main__":
    # find files in the directory
    resume_pdfs, job_html, file_names = get_files()

    # extract text for job description and resumes
    resume_texts = get_resume_texts(resume_pdfs)
    job_text = get_job_text(job_html)

    # combine all the texts extracted into one list
    combined_texts = list(resume_texts)
    combined_texts.append(job_text)

    # send them to openai to be embedded and separate embeddings
    resume_embeddings, job_embedding = get_embedding(combined_texts)
