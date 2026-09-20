from pathlib import Path
import shutil

from fastapi import UploadFile


LECTURE_STORAGE_DIR = Path("data/lectures")


def save_uploaded_lecture(file: UploadFile) -> Path:
    """
    Save an uploaded lecture file to the application's lecture storage directory.
    """

    LECTURE_STORAGE_DIR.mkdir(parents=True, exist_ok=True)

    destination = LECTURE_STORAGE_DIR / file.filename

    with destination.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return destination