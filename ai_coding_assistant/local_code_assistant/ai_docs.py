from .ollama_client import ask_model

def generate_ai_docs(code):

    prompt = f"""
Generate ONLY a Python docstring.

Format:

\"\"\"
Short description.

Args:
    param: description

Returns:
    description
\"\"\"

Code:
{code}
"""

    return ask_model(prompt)