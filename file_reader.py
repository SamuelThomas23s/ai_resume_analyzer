import os
import PyPDF2

def read_file(path):
    if not os.path.exists(path):
        return None

    if path.endswith(".txt"):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    if path.endswith(".pdf"):
        text = ""

        with open(path, "rb") as f:
            reader = PyPDF2.PdfReader(f)

            for page in reader.pages:
                text += page.extract_text() or ""

        return text

    return None