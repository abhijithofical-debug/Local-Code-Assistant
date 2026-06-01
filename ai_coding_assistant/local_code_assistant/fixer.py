from .ollama_client import ask_model

def fix_code(code, error):

    prompt = f"""
You are a Python code fixer.

Rules:
- Return ONLY corrected Python code.
- No explanations.
- No markdown.
- No comments.
- No code fences.

Error:
{error}

Code:
{code}
"""

    return ask_model(prompt)