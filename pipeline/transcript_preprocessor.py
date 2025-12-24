import re
from data.models import Transcript

class TranscriptPreprocessor:
    def preprocess(self, transcript: Transcript) -> str:
        if not transcript.segments:
            return ""

        # Join all ASR segments
        text = " ".join(seg.text for seg in transcript.segments)

        # Normalize whitespace
        text = re.sub(r"\s+", " ", text).strip()

        # Remove obvious repeated fillers at the start
        text = re.sub(
            r"^(hello|hi|okay|so|yeah)(\s+\1)+",
            r"\1",
            text,
            flags=re.IGNORECASE,
        )

        return text
