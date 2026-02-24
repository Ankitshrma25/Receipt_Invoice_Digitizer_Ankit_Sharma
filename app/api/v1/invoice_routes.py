from fastapi import APIRouter, UploadFile, File
import os
import shutil
from app.services.ocr_service import extract_text_from_image

router = APIRouter(prefix="/invoice", tags=["invoice"])

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(upload_dir, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # OCR service
    extracted_text = extract_text_from_image(file_path)

    return {
        "filename": file.filename,
        "extracted_text": extracted_text
    }