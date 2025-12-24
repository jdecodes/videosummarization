from pipeline.app_context import create_prompt_builder
from pipeline.llm_description_generator import LLMDescriptionGenerator
from pipeline.logger import Logger
from pipeline.logging_context import logger
from pipeline.video_loader import VideoLoader
from pipeline.video_to_audio import VideoToAudioConverter
from pipeline.audio_to_speech import AudioToSpeech
from pipeline.speech_analyzer import SpeechAnalyzer
from data.models import VideoDescription
from pipeline.timing import time_block

class VideoSummarizer:
    def __init__(self, llm_generator: LLMDescriptionGenerator):
        self.llm_generator = llm_generator
        self.video_loader = VideoLoader()
        self.video_to_audio = VideoToAudioConverter()
        self.audio_to_speech = AudioToSpeech()
        self.speech_analyzer = SpeechAnalyzer(self.llm_generator)

    def summarize(self, video_path: str) -> VideoDescription:
        timings = {}

        with time_block("load_video", timings):
            logger.info("Loading video")
            video = self.video_loader.load(video_path)

        with time_block("video_to_audio", timings):
            logger.info("convert video to audio")
            audio = self.video_to_audio.convert(video)

        with time_block("audio_to_speech", timings):
            logger.info("convert audio file to text")
            transcript = self.audio_to_speech.transcribe(audio)

        with time_block("describe_with_llm", timings):
            logger.info("convert text with llm")
            description = self.speech_analyzer.describe(transcript)

        print("\n=== SUMMARY TIMINGS ===")
        for k, v in timings.items():
            print(f"{k:20s}: {v:.3f}s")

        return description

