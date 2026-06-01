from .ollama_client import ask_model
import re

def complete_code(code):

    lines = code.strip().split("\n")

    last_line = lines[-1].strip()

    # Rule-based completions

    if last_line.startswith("for ") and last_line.endswith(":"):

        match = re.search(r"for\s+(\w+)\s+in", last_line)

        if match:
            variable = match.group(1)
            return f"    print({variable})"

        return "    pass"

    if last_line.startswith("if ") and last_line.endswith(":"):
        return "    pass"

    if last_line.startswith("def ") and last_line.endswith(":"):
        return "    pass"

    print("Using AI fallback...")

    prompt = f"""
You are a Python code completion engine.

Return ONLY the next line of Python code.

Code:
{code}

Next line:
"""

    return ask_model(prompt)