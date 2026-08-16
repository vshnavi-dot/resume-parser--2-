# Resume Parser

*Intern ID:* CITS8349
*NAME:* VAISHNAVI
*Number of Weeks:* 4
*Project Name:* Resume Parser

A simple web app that extracts structured information (name, email, phone, skills, education) from uploaded resumes (PDF/DOCX) using Flask + regex/keyword matching.


## Project Scope
This project was built as a 4-week internship deliverable to demonstrate a working, end-to-end resume screening tool. The scope covers:
- Accepting resume uploads in PDF and DOCX formats through a simple web interface
- Extracting key candidate details (name, email, phone, skills, education) using text extraction and regex/keyword matching — no external ML model required
- Presenting the extracted results back to the user in a readable format
- Packaging the project for easy local setup and future deployment

Out of scope for this version: advanced NLP-based entity recognition, resume scoring against job descriptions, batch/bulk resume processing, and a persistent database — these are listed under Future Improvements below as natural next steps.



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
   git clone https://github.com/vshnavi-dot/resume-parser.git
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
Vaishnavi — [GitHub](https://github.com/vshnavi-dot) | [LinkedIn](https://www.linkedin.com/in/vaishnavi-acharya-1955a933b?utm_source=share_via&utm_content=profile&utm_medium=member_android)
