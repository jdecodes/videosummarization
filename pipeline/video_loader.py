from data.models import Video


class VideoLoader:
    def load(self, video_path: str) -> Video:
        # Future: validate existence, duration, codec, etc.
        return Video(path=video_path)
