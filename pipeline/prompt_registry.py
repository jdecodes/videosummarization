from pipeline.prompt_template import PromptTemplate

VIDEO_SUMMARY_V1 = PromptTemplate(
    name="video_summary_v1",
    min_words=100,
    max_words=300,
    template="""
You are rewriting content for a learning summary.

Task:
Write a clear and simple summary of the content below.

Rules:
- Use between 90 and 110 words.
- Do not exceed 110 words.
- Cover all major ideas mentioned in the content.
- Do not add new information or examples.
- Remove repetition and headings.
- Use plain, beginner-friendly language.

Process:
1. Identify the key points that must be included.
2. Write the summary.
3. Revise the summary to ensure it stays within the word limit.

Content:
\"\"\"
{{TEXT}}
\"\"\"
""".strip(),
)
