from typing import Dict
from pipeline.prompt_template import PromptTemplate


class PromptBuilder:
    """
    Responsible for registering prompt templates and
    building final prompts by injecting content.
    """

    def __init__(self, system_prompt: str):
        self._templates: Dict[str, PromptTemplate] = {}
        self.system_prompt = system_prompt.strip()

    def register(self, prompt: PromptTemplate) -> None:
        if prompt.name in self._templates:
            raise ValueError(f"Prompt '{prompt.name}' already registered")
        self._templates[prompt.name] = prompt

    def build(self, name: str, text: str) -> PromptTemplate:
        if name not in self._templates:
            raise ValueError(f"Prompt '{name}' is not registered")

        base = self._templates[name]

        filled_template = base.template.replace(
            "{{TEXT}}",
            text.strip()
        )

        return PromptTemplate(
            name=base.name,
            template=filled_template,
            min_words=base.min_words,
            max_words=base.max_words,
        )
