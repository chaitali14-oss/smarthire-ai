
# SmartHire AI

An AI-powered Resume Screening and Career Recommendation System.

## Project Objective

SmartHire AI aims to help job seekers compare their resumes with job descriptions, identify missing skills, and receive personalized career recommendations.

## Planned Features

- Resume PDF text extraction
- Resume-to-job similarity matching
- Machine learning job-category classification
- LLM-powered career recommendations
- Retrieval-Augmented Generation (RAG)
- FastAPI backend
- Streamlit dashboard
- SQLite database

## Technology Stack

- Python 3.11
- PyMuPDF
- SQLite
- Pytest
- NumPy and Pandas (planned)
- Scikit-learn (planned)
- Generative AI and RAG (planned)
- FastAPI and Streamlit (planned)
- Git and GitHub

## Current Features

- Extract text from PDF resumes using PyMuPDF.
- Process text across multiple PDF pages.
- Handle missing files and invalid file types.
- Detect PDFs with no extractable text.
- Normalize whitespace and remove unwanted control characters from resume text.
- Store resume filenames and cleaned text in SQLite.
- Retrieve stored resume records by ID.
- Process extracted resume text through a cleaning and storage service.
- Automated tests for parsing, cleaning, database operations, and resume processing.

## Installation

1. Clone this repository.
2. Create and activate a Python virtual environment.
3. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

4. Install pytest if it is not already installed:

   ```powershell
   python -m pip install pytest
   ```

## Run the Application

Activate the virtual environment and run:

```powershell
python app.py
```

## Database

SmartHire AI uses Python's built-in SQLite support to store resume metadata and cleaned resume text in `data/smarthire.db`.

The `resumes` table contains:

- Resume ID
- Original filename
- Cleaned resume text
- Creation timestamp

The database and table are initialized automatically when records are inserted or retrieved.

## Run Tests

Run the complete test suite:

```powershell
python -m pytest -v
```

Tests use temporary databases to avoid adding test records to the default database.

## Privacy

Never commit API keys, private credentials, or real resumes containing personal information to this public repository.

## Disclaimer

This is an educational portfolio project. Resume similarity scores are not probabilities of being hired.

## Project Progress

## Development Progress

- **Day 1:** Project structure, Python environment, and initial tests.
- **Day 2:** PDF resume text extraction using PyMuPDF.
- **Day 3:** Text cleaning, SQLite storage, and integrated resume processing.
- **Day 4:** Structured resume information extraction, including skills, education, emails, and phone numbers.
- **Day 5:** Add the verified milestone once confirmed.
- **Day 6:** Resume-to-job skill matching with matched skills, missing skills, and an explainable overlap score.
- **Day 7:** SQLite-integrated saved-resume matching service with input validation and automated tests.

**Testing:** 19 tests passed in the latest verified full test run.