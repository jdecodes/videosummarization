from pipeline.prompt_builder import PromptBuilder
from pipeline.system_prompts import SUMMARY_SYSTEM_PROMPT
from pipeline.prompt_registry import VIDEO_SUMMARY_V1


def create_prompt_builder() -> PromptBuilder:
    print("creating prompt builder")
    prompt_builder = PromptBuilder(
        system_prompt=SUMMARY_SYSTEM_PROMPT
    )
    prompt_builder.register(VIDEO_SUMMARY_V1)

    return prompt_builder
