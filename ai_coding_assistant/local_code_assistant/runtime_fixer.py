from .runtime_checker import check_runtime
from .ollama_client import ask_model


def fix_runtime_error(code):

    result = check_runtime(code)

    if result["success"]:
        return code

    prompt = f"""
You are a Python code fixer.

Rules:
- Return ONLY corrected Python code.
- No explanations.
- No markdown.
- No comments.

Error Type:
{result['error_type']}

Error Message:
{result['message']}

Code:
{code}
"""

    return ask_model(prompt)