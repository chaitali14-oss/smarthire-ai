
# SmartHire AI

An AI-powered Resume Screening and Career Recommendation System.

## Project Objective

SmartHire AI aims to help job seekers compare their resumes with job
descriptions, identify missing skills, and receive personalized
career recommendations.

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

- Python
- NumPy and Pandas
- Scikit-learn
- Generative AI and RAG
- FastAPI and Streamlit
- SQLite
- Git and GitHub

## Current Progress

Day 1: Project setup, welcome application, and three passing unit tests.

## Run the Application

Activate the virtual environment and run:

    python app.py

## Run Tests

    python -m unittest discover -s tests -v

## Privacy

Never commit API keys, private credentials, or real resumes containing
personal information to this public repository.

## Disclaimer

This is an educational portfolio project. Similarity scores are not
probabilities of being hired.



## Current Features

- Extract text from PDF resumes using PyMuPDF.
- Process text across multiple PDF pages.
- Handle missing files and invalid file types.
- Detect PDFs with no extractable text.
- Automated unit tests for resume parsing and error handling.

## Installation

1. Clone this repository.
2. Create and activate a Python virtual environment.
3. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

## Run Tests

```bash
python -m unittest discover -s tests -v
```

## Current Status

Day 2: PDF resume text extraction implemented and tested.
