from pathlib import Path


SUPPORTED_AUDIO_EXTENSIONS = {".mp3", ".wav", ".m4a"}
SUPPORTED_VIDEO_EXTENSIONS = {".mp4", ".mkv", ".mov"}


def validate_lecture_file(file_path: str) -> bool:
    """
    Check whether the lecture file has a supported extension.
    """

    path = Path(file_path)

    extension = path.suffix.lower()

    return (
        extension in SUPPORTED_AUDIO_EXTENSIONS
        or extension in SUPPORTED_VIDEO_EXTENSIONS
    )