from ollama import chat

import time

system_prompt = """
You are a careful and disciplined summarization assistant.

Your role is to rewrite provided content into clear, accurate learning summaries.

Rules you must always follow:
- Do not add information that is not present in the input.
- Do not remove important ideas or topics.
- Prefer completeness over creativity.
- Use simple, beginner-friendly language.
- Avoid marketing language, opinions, or speculation.
- If information is unclear or repetitive, simplify it without changing meaning.

You must follow all formatting and length constraints given by the user.
"""

user_prompt = f"""You are rewriting content for a learning summary. 

Task:
Write a clear and simple summary of the content below.

Rules:
 Use between 90 and 110 words.
 Cover all major ideas mentioned in the content.
 Do not add new information or examples.
 Remove repetition and headings.
 Use plain, beginner-friendly language.

Process:
 First, decide the key points that must be included.
 Then write the summary.
 Finally, revise the summary to ensure it stays within the word limit.
"""

def make_user_prompt(input_txt) :
    return f"""
        {user_prompt} 
        Content:
        \"\"\"
        {input_txt}
        \"\"\"
        """

def get_input_from_file() :
    input_txt = ""
    with open("content_to_summarize.txt") as f:
        file_txt = f.read()
        for line in file_txt.split("\n"):
            input_txt += line
    return input_txt


def get_input():
    return get_input_from_file()

def test_describe() :
    input_txt = get_input()
    user_prompt_text = make_user_prompt(input_txt)

    response = chat(
        model="phi3:mini",
        messages=[
            {
                "role": "system",
                "content": f"{system_prompt}"
            },
            {
                "role": "user",
                "content": f"{user_prompt_text}"
            }
        ]
    )
    print(response["message"]["content"])


def test_ollam() :
    print(f" start the model")
    start_time = time.time()
    test_describe()
    end_time = time.time()
    time_taken = end_time - start_time
    print(f"completed in {time_taken:.4f} seconds.")

test_ollam()
