from .ollama_client import ask_model

def suggest_alternatives(code):

    prompt = f"""
Return ONLY Python code.

No comments.
No explanation.
No markdown.

Code:

{code}
"""

    return ask_model(prompt)