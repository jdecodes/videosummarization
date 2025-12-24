from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class PromptTemplate:
    """
    Immutable definition of a prompt.
    This is configuration, not behavior.
    """
    name: str
    template: str
    min_words: Optional[int] = None
    max_words: Optional[int] = None
