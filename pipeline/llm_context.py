from pipeline.app_context import create_prompt_builder
from pipeline.llm_description_generator import LLMDescriptionGenerator

def create_llm_gen():
    prompt_builder = create_prompt_builder()
    llm_gen = LLMDescriptionGenerator(prompt_builder)
    return llm_gen