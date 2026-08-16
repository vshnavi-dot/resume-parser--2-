"""
app.py
------
Flask web app for the resume parser.

Routes:
- GET  /        -> Upload form
- POST /upload  -> Accepts a resume file, parses it, shows results
"""

import os
from flask import Flask, request, render_template

from resume_parser import parse_resume

app = Flask(__name__)

ALLOWED_EXTENSIONS = {"pdf", "docx"}
MAX_FILE_SIZE_MB = 5
app.config["MAX_CONTENT_LENGTH"] = MAX_FILE_SIZE_MB * 1024 * 1024


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    if "resume" not in request.files:
        return render_template("index.html", error="No file part in the request.")

    file = request.files["resume"]

    if file.filename == "":
        return render_template("index.html", error="No file selected.")

    if not allowed_file(file.filename):
        return render_template("index.html", error="Only .pdf and .docx files are supported.")

    try:
        file_bytes = file.read()
        result = parse_resume(file.filename, file_bytes)
        return render_template("index.html", result=result, filename=file.filename)
    except Exception as e:
        return render_template("index.html", error=f"Failed to parse resume: {str(e)}")


if __name__ == "__main__":
    # debug=True is fine for local dev; turn off before any real deployment
    app.run(debug=True, port=5000)
