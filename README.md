
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

### Day 1: Project Setup and Initial Testing
- Created the SmartHire AI project structure.
- Set up the Python environment and project dependencies.
- Created the initial application entry point (`app.py`).
- Added `README.md`, `requirements.txt`, and `.gitignore`.
- Created initial unit tests and verified the project setup.

### Day 2: PDF Resume Text Extraction
- Implemented PDF text extraction using PyMuPDF.
- Created `resume_parser.py` to extract text from resume PDFs.
- Added handling for missing files, invalid file types, and PDFs without extractable text.
- Tested resume parsing functionality.

### Day 3: Resume Text Cleaning and SQLite Storage
- Implemented resume text cleaning and normalization.
- Created `text_cleaner.py` to normalize whitespace and remove unwanted control characters.
- Implemented SQLite database operations in `database.py`.
- Created `resume_service.py` to integrate resume processing, cleaning, and storage.
- Added automated tests for text cleaning, database operations, and resume processing.

### Day 4: Structured Resume Information Extraction
- Created `resume_extractor.py`.
- Implemented extraction of email addresses and phone numbers.
- Added technical skill and education extraction.
- Tested the resume information extraction functionality.

### Day 5: [Confirm the completed milestone]
- Update this section with the exact feature implemented and tested on Day 5.

### Day 6: Resume-to-Job Skill Matching
- Created `job_matcher.py` to compare resume skills against job requirements.
- Implemented matched-skill and missing-skill identification.
- Added a skill-overlap match score.
- Tested full matches, partial matches, case-insensitive matching, invalid inputs, and job descriptions without recognized skills.

### Day 7: Saved Resume–Job Matching Service
- Created `job_match_service.py` to match a saved resume against a job description.
- Integrated SQLite resume retrieval with the skill-matching functionality.
- Returned the resume ID, filename, match score, matched skills, and missing skills.
- Added input validation and handling for missing resume records.
- Added automated tests for the service.
- Verified that all 19 project tests passed.

### Current Project Status
- PDF resume parsing, text cleaning, and SQLite storage implemented.
- Structured resume information extraction implemented.
- Resume-to-job skill matching implemented.
- Saved-resume matching service integrated and tested.
- **Latest verified test result: 19 tests passed.**

### Upcoming Milestones
- Day 8: Build the FastAPI backend and expose resume-matching functionality through REST endpoints.
- Upcoming: Add machine learning-based job-category classification.
- Upcoming: Integrate LLM-powered career recommendations and Retrieval-Augmented Generation (RAG).
- Upcoming: Develop a Streamlit dashboard.
- Upcoming: Add broader integration tests and deployment support.

