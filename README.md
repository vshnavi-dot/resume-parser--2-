# Resume Parser

A simple web app that extracts structured information (name, email, phone, skills, education) from uploaded resumes (PDF/DOCX) using Flask + regex/keyword matching.

## Features
- Upload a `.pdf` or `.docx` resume through a browser
- Extracts:
  - Candidate name (best-effort)
  - Email address
  - Phone number
  - Matched skills (from a predefined keyword list)
  - Education-related lines
- Simple, dependency-light implementation — no ML model required

## Tech Stack
- **Backend:** Python, Flask
- **Parsing:** PyPDF2 (PDF text extraction), python-docx (DOCX text extraction), regex
- **Frontend:** Plain HTML/CSS (Jinja2 templates)

## Project Structure
```
resume-parser/
├── app.py               # Flask routes
├── resume_parser.py     # Core text extraction & field parsing logic
├── requirements.txt     # Python dependencies
├── templates/
│   └── index.html       # Upload form + results page
└── uploads/              # (empty, .gitignored) local test uploads
```

## Running Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/tkp278/resume-parser.git
   cd resume-parser
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python app.py
   ```

4. Open your browser at `http://127.0.0.1:5000`

## Future Improvements
- Add NLP-based (spaCy) name/entity extraction for better accuracy
- Expand skill keyword list or load it from a config file
- Add resume scoring against a job description
- Export parsed results as JSON/CSV

## Author
Tejas Poojary — [GitHub](https://github.com/tkp278) | [LinkedIn](https://linkedin.com/in/tejas-poojary)
