from ollama import chat

from pipeline.app_context import create_prompt_builder
from pipeline.prompt_builder import PromptBuilder
#from pipeline.output_validator import OutputValidator


class LLMDescriptionGenerator:
    def __init__(
        self,
        prompt_builder: PromptBuilder,
        model_name: str = "phi3:mini",
    ):
        self.prompt_builder = prompt_builder
        self.model_name = model_name

    def generate(self, text: str, prompt_name: str) -> str:
        prompt = self.prompt_builder.build(prompt_name, text)
        print(f" generate with llm ")
        #print(f" system prompt {self.prompt_builder.system_prompt} ")
        #print(f" user prompt {prompt.template} ")
        response = chat(
            model=self.model_name,
            messages=[
                {
                    "role": "system",
                    "content": self.prompt_builder.system_prompt,
                },
                {
                    "role": "user",
                    "content": prompt.template,
                },
            ],
        )

        output = response["message"]["content"].strip()

        # if not OutputValidator.validate_word_limit(
        #     output,
        #     prompt.min_words,
        #     prompt.max_words,
        # ):
        #     raise ValueError(
        #         f"LLM output violates word limit "
        #         f"({OutputValidator.word_count(output)} words)"
        #     )

        return output
