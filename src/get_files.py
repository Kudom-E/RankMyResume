import os


# get all pdf and html files in designated directory
def get_files(max_retries=None):
    attempts = 0
    while True:
        if max_retries is not None and attempts >= max_retries:
            raise IndexError("❌ Max retries reached. Exiting.")

        # request for directory
        designated_directory = input(
            r"Enter the single directory:("
            r"eg: all files in C:\Users\UserName\Documents\Resumes, "
            "enter Documents/Resumes):\n~/")

        if not designated_directory:
            print("❌ No directory entered. Please enter a valid path.")
            attempts += 1
            continue

        if os.path.exists(os.path.expanduser(
                "~/"+designated_directory.strip())):

            path = os.path.expanduser('~/'+designated_directory.strip())
            print(f"✅ Directory set to: "
                  f"{os.path.abspath(path)}"
                  )
            break
        else:
            print("❌ Invalid directory. Please check the path and try again.")
            attempts += 1

    # change directory to provided directory
    os.chdir(os.path.expanduser("~/"+designated_directory.strip()))

    # find files in directory
    files = [
        entry.name for entry in os.scandir()
        if entry.name.lower() != "desktop.ini"
        and entry.name.lower().endswith(".pdf")
        or entry.name.lower().endswith(".html")
    ]

    if not files:
        raise ValueError("❌ No PDF or HTML files found in the directory.")

    resume_pdfs = [file for file in files if file.endswith(".pdf")]
    job_html = [file for file in files if file.endswith(".html")]

    if len(job_html) > 1:
        raise ValueError(
            "You have more than one job file, you will have to remove one"
        )
    else:
        return resume_pdfs, job_html
