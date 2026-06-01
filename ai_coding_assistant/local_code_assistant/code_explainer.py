from .ollama_client import ask_model


def explain_code(code):

    prompt = f"""
Explain this Python code for a beginner.

Rules:
- Explain line by line.
- Keep it short.
- Mention the output.
- No markdown.

Code:
{code}
"""

    return ask_model(prompt)