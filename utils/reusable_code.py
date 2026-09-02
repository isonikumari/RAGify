import os
import shutil
from pathlib import Path
import yt_dlp
from pydub import AudioSegment

FFMPEG_PATHS = [
    r"C:\Users\misha\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0-full_build\bin",
    r"C:\Program Files\ffmpeg\bin",
    r"C:\Program Files (x86)\ffmpeg\bin",
]

def ensure_ffmpeg():
    current_path = os.environ.get("PATH", "")
    for folder in FFMPEG_PATHS:
        if os.path.isdir(folder) and folder not in current_path.split(os.pathsep):
            os.environ["PATH"] = folder + os.pathsep + current_path
            current_path = os.environ["PATH"]

    if shutil.which("ffmpeg") is None:
        raise RuntimeError(
            "FFmpeg is missing. Install it and make sure it is in PATH."
        )

def download_audio(url: str, output_dir: str = "downloades") -> str:
    ensure_ffmpeg()

    out_dir = Path(output_dir)
    out_dir.mkdir(exist_ok=True)

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": str(out_dir / "%(title)s.%(ext)s"),
        "noplaylist": True,
        "quiet": True,
        "no_warnings": True,
        "extractor_args": {
            "youtube": {
                "player_client": ["web", "android", "tv_embedded"]
            }
        },
        "http_headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        },
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "wav",
            "preferredquality": "0"
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)

    title = info.get("title", "audio")
    file_name = f"{title}.wav"
    return str(out_dir / file_name)

def load_audio(file_path: str) -> AudioSegment:
    audio = AudioSegment.from_wav(file_path)
    print(f"Loaded: {file_path}")
    print(f"Duration: {len(audio) / 1000:.2f} seconds")
    return audio

if __name__ == "__main__":
    sample_url = "https://www.youtube.com/watch?v=aqz-KE-bpKQ"
    wav_path = download_audio(sample_url)
    audio = load_audio(wav_path)


#     What this does:

# downloads the YouTube audio
# converts it to WAV automatically
# loads the WAV file with pydub
# shows the duration of the file
# Note:

# The sample URL is known to work.
# Some other YouTube links may still fail with 403 due to YouTube restrictions.
# # If you want, I can also(
# If you want, I can also give you the next version with:

# trimming audio
# splitting into chunks
# saving clips for transcription
# # better file naming)