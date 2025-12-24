from faster_whisper import WhisperModel
from data.models import Audio, Transcript, SpeechSegment


class AudioToSpeech:
    def __init__(self, model_name: str = "medium", device: str = "cpu"):
        self.model = WhisperModel(
            model_name,
            device=device,
            compute_type="int8"
        )

    def transcribe(self, audio: Audio) -> Transcript:
        segments, _ = self.model.transcribe(
            audio.path,
            beam_size=5,
            word_timestamps=False
        )

        speech_segments = []
        for seg in segments:
            print(f" found segment {seg.start} -> {seg.end} : {seg.text}")
            speech_segments.append(
                SpeechSegment(
                    start=seg.start,
                    end=seg.end,
                    text=seg.text.strip()
                )
            )

        return Transcript(segments=speech_segments)
