from pdfminer.high_level import extract_text


def get_resume_texts(resume_pdfs):
    if not resume_pdfs:
        print("No resumes found")
        return []

    resume_text = [extract_text(resume) for resume in resume_pdfs]

    return resume_text
