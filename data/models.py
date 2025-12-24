from dataclasses import dataclass
from typing import List


@dataclass
class Video:
    path: str


@dataclass
class Audio:
    path: str


@dataclass
class SpeechSegment:
    start: float
    end: float
    text: str


@dataclass
class Transcript:
    segments: List[SpeechSegment]


@dataclass
class VideoDescription:
    text: str
