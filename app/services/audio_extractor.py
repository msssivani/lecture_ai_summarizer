from pathlib import Path
import subprocess


AUDIO_STORAGE_DIR = Path("data/audio")


def extract_audio(video_path: str) -> Path:
    """
    Extract audio from a lecture video using FFmpeg.
    """

    video = Path(video_path)

    if not video.exists():
        raise FileNotFoundError(f"Video file not found: {video}")

    AUDIO_STORAGE_DIR.mkdir(parents=True, exist_ok=True)

    audio_path = AUDIO_STORAGE_DIR / f"{video.stem}.wav"

    command = [
        "ffmpeg",
        "-i",
        str(video),
        "-vn",
        "-acodec",
        "pcm_s16le",
        str(audio_path),
    ]

    subprocess.run(command, check=True)

    return audio_path