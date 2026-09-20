from pathlib import Path
import shutil


LECTURE_STORAGE_DIR = Path("data/lectures")


def save_lecture_file(source_path: str) -> Path:
    """
    Move a lecture file into the application's lecture storage directory.
    """

    source = Path(source_path)

    if not source.exists():
        raise FileNotFoundError(f"Lecture file not found: {source}")

    LECTURE_STORAGE_DIR.mkdir(parents=True, exist_ok=True)

    destination = LECTURE_STORAGE_DIR / source.name

    shutil.move(source, destination)

    return destination