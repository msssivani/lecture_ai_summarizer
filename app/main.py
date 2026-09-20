from fastapi import FastAPI, UploadFile, File

from app.services.file_storage import save_uploaded_lecture


app = FastAPI(
    title="Lecture AI",
    description="AI-powered lecture processing system",
    version="0.1.0",
)


@app.post("/lectures/upload")
async def upload_lecture(file: UploadFile = File(...)):
    saved_path = save_uploaded_lecture(file)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "saved_path": str(saved_path),
    }