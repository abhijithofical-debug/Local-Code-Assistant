from .ollama_client import ask_model

def generate_docs(code):

    prompt = f"""
Generate documentation for this Python code.

Code:
{code}
"""

    return ask_model(prompt)