import io
import pdfplumber
import docx

def extract_text_from_pdf(file_bytes) -> str:
    text = ""
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()

def extract_text_from_docx(file_bytes) -> str:
    doc = docx.Document(io.BytesIO(file_bytes))
    full_text = [para.text for para in doc.paragraphs if para.text.strip()]
    return "\n".join(full_text).strip()

def extract_text(file_name: str, file_bytes: bytes) -> str:
    if file_name.lower().endswith(".pdf"):
        return extract_text_from_pdf(file_bytes)
    elif file_name.lower().endswith(".docx"):
        return extract_text_from_docx(file_bytes)
    else:
        # Fallback to plain text decode
        return file_bytes.decode("utf-8", errors="ignore").strip()