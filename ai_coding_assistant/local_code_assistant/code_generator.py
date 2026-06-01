from .ollama_client import ask_model


def generate_code(user_prompt):

    prompt = f"""
Generate Python code.

Rules:
- Return ONLY executable Python code.
- No markdown.
- No explanations.
- No comments.
- No code fences.

Task:
{user_prompt}
"""

    return ask_model(prompt)