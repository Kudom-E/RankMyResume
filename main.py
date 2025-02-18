import os
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


def get_resume_texts(resumes):
    if not resumes:
        print("No resumes found")
        return []

    resume_text = [extract_text(resume) for resume in resumes]

    return resume_text


if __name__ == "__main__":
    get_files()
