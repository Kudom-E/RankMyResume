import os
import re
import bs4
from pdfminer.high_level import extract_text


# get all pdf and html files in designated directory
def get_files():
    # request for directory
    designated_directory = input(
        r"Enter the single directory:(eg: all files in C:\Users\UserName\Documents\Resumes, "
        "enter Documents/Resumes):\n~/")

    # change directory to provided directory
    os.chdir(os.path.expanduser("~/"+designated_directory))

    # find files in directory
    files = [
        entry.name for entry in os.scandir()
        if entry.name.lower() != "desktop.ini" and entry.name.lower().endswith(".pdf")
        or entry.name.lower().endswith(".html")
    ]

    print(files)
    return files


def get_resume_texts(resume_pdfs):
    if not resume_pdfs:
        print("No resumes found")
        return []

    resume_text = [extract_text(resume) for resume in resume_pdfs]

    return resume_text


def get_job_text(job_html):
    if not job_html:
        print("No job description found")
        return

    with open(job_html, "r", encoding="utf-8") as job_descript:
        html_content = job_descript.read()

    soup = bs4.BeautifulSoup(html_content, "html.parser")
    text = soup.find("main")

    if text:
        text = text.get_text()
    else:
        text = soup.get_text()

    # Replace multiple spaces with one space
    cleaned_text = re.sub(r'\s{2,}', ' ', text)

    # Replace multiple newlines with one
    cleaned_text = re.sub(r'\n+', '\n', cleaned_text)

    cleaned_text = cleaned_text.strip()

    return cleaned_text



if __name__ == "__main__":
    get_files()
