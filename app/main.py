from fastapi import FastAPI, UploadFile, File


app = FastAPI(
    title="Lecture AI",
    description="AI-powered lecture processing system",
    version="0.1.0",
)


@app.post("/lectures/upload")
async def upload_lecture(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type,
    }