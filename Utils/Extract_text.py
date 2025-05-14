from PyPDF2 import PdfReader
import io


def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(io.BytesIO(uploaded_file.read()))
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text