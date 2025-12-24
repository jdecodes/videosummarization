import subprocess
import os
from data.models import Video, Audio


class VideoToAudioConverter:
    def __init__(self, output_dir: str = "artifacts"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def convert(self, video: Video) -> Audio:
        audio_path = os.path.join(self.output_dir, "audio.wav")

        cmd = [
            "ffmpeg",
            "-y",
            "-i", video.path,
            "-vn",
            "-acodec", "pcm_s16le",
            "-ar", "16000",
            "-ac", "1",
            audio_path
        ]

        subprocess.run(cmd, check=True)
        return Audio(path=audio_path)
