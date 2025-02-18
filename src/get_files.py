import os


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

    return files
