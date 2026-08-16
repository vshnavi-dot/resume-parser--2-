"""
resume_parser.py
-----------------
Core logic for extracting structured information from resume files (PDF/DOCX).

Approach:
1. Extract raw text depending on file type (PyPDF2 for .pdf, python-docx for .docx)
2. Run regex / keyword matching over the raw text to pull out:
   - Name (best-effort: first non-empty line)
   - Email
   - Phone number
   - Skills (matched against a predefined skill keyword list)
   - Education (lines containing common degree keywords)
"""

import re
import io
import docx
from PyPDF2 import PdfReader

# A small predefined skill list to match against.
# Extend this list with more keywords relevant to your target roles.
SKILL_KEYWORDS = [
    "python", "java", "c++", "c", "javascript", "typescript", "react", "node.js",
    "flask", "django", "sql", "mysql", "postgresql", "mongodb", "git", "github",
    "html", "css", "aws", "azure", "docker", "kubernetes", "linux",
    "machine learning", "deep learning", "tensorflow", "pytorch", "keras",
    "embedded systems", "stm32", "arduino", "verilog", "matlab", "vhdl",
    "microcontroller", "firmware", "iot", "rtos", "excel", "power bi",
    "communication", "leadership", "teamwork", "problem solving"
]

EDUCATION_KEYWORDS = [
    "b.tech", "btech", "bachelor", "m.tech", "mtech", "master",
    "b.e", "be ", "m.e", "phd", "diploma", "engineering", "university", "college"
]

EMAIL_REGEX = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
PHONE_REGEX = r'(\+?\d{1,3}[-.\s]?)?\(?\d{3,5}\)?[-.\s]?\d{3}[-.\s]?\d{3,4}'


def extract_text_from_pdf(file_stream):
    """Extract all text from a PDF file-like object."""
    reader = PdfReader(file_stream)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text


def extract_text_from_docx(file_stream):
    """Extract all text from a DOCX file-like object."""
    document = docx.Document(file_stream)
    return "\n".join(p.text for p in document.paragraphs)


def extract_text(filename, file_stream):
    """Dispatch to the right extractor based on file extension."""
    filename = filename.lower()
    if filename.endswith(".pdf"):
        return extract_text_from_pdf(file_stream)
    elif filename.endswith(".docx"):
        return extract_text_from_docx(file_stream)
    else:
        raise ValueError("Unsupported file type. Please upload a .pdf or .docx file.")


def extract_email(text):
    match = re.search(EMAIL_REGEX, text)
    return match.group(0) if match else None


def extract_phone(text):
    match = re.search(PHONE_REGEX, text)
    return match.group(0).strip() if match else None


def extract_name(text):
    """Best-effort: assume the first non-empty line is the candidate's name."""
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    if lines:
        # Avoid picking up a line that's actually an email/phone/address
        for line in lines[:3]:
            if not re.search(EMAIL_REGEX, line) and not re.search(r'\d{5,}', line):
                return line
    return None


def extract_skills(text):
    text_lower = text.lower()
    found = [skill for skill in SKILL_KEYWORDS if skill in text_lower]
    return sorted(set(found))


def extract_education(text):
    lines = text.split("\n")
    matches = []
    for line in lines:
        line_lower = line.lower()
        if any(keyword in line_lower for keyword in EDUCATION_KEYWORDS):
            cleaned = line.strip()
            if cleaned:
                matches.append(cleaned)
    return matches


def parse_resume(filename, file_bytes):
    """
    Main entry point. Takes the filename and raw bytes of the uploaded file,
    returns a dictionary of extracted fields.
    """
    file_stream = io.BytesIO(file_bytes)
    text = extract_text(filename, file_stream)

    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text),
        "education": extract_education(text),
        "raw_text_preview": text[:500]  # first 500 chars, useful for debugging
    }
