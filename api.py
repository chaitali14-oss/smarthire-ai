
from pathlib import Path
from tempfile import NamedTemporaryFile

from fastapi import FastAPI, File, HTTPException, UploadFile

from resume_parser import extract_text_from_pdf
from resume_service import process_resume_with_profile

app = FastAPI(
    title="SmartHire AI API",
    description="API for resume screening and job matching.",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "message": "Welcome to SmartHire AI API",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "SmartHire AI API",
    }


@app.post("/upload-resume")
def upload_resume(file: UploadFile = File(...)):
    """Upload a PDF resume, extract its text, and save its profile."""
    if not file.filename or Path(file.filename).suffix.lower() != ".pdf":
        raise HTTPException(
            status_code=400,
            detail="Please upload a PDF resume.",
        )

    temp_path = None

    try:
        with NamedTemporaryFile(
            suffix=".pdf",
            delete=False,
        ) as temp_file:
            temp_path = Path(temp_file.name)

            while chunk := file.file.read(1024 * 1024):
                temp_file.write(chunk)

        extracted_text = extract_text_from_pdf(temp_path)

        result = process_resume_with_profile(
            filename=Path(file.filename).name,
            extracted_text=extracted_text,
        )

        return {
            "message": "Resume uploaded and processed successfully.",
            **result,
        }

    except (ValueError, FileNotFoundError) as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    finally:
        file.file.close()

        if temp_path is not None:
            temp_path.unlink(missing_ok=True)
