from data.models import Transcript, VideoDescription
from pipeline.logging_context import logger
from pipeline.transcript_preprocessor import TranscriptPreprocessor
from pipeline.llm_description_generator import LLMDescriptionGenerator


class SpeechAnalyzer:
    def __init__(self, llm_generator: LLMDescriptionGenerator):
        self.preprocessor = TranscriptPreprocessor()
        self.llm_generator = llm_generator

    def describe(self, transcript: Transcript) -> VideoDescription:

        logger.info("preprocessing transcript")
        raw_text = self.preprocessor.preprocess(transcript)

        if not raw_text:
            return VideoDescription(
                text="This video does not contain any detectable speech."
            )
        logger.info("generate with llm")
        description = self.llm_generator.generate(
            raw_text,
            prompt_name="video_summary_v1",
        )

        return VideoDescription(text=description)
