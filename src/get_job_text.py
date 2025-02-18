import re
import bs4


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
