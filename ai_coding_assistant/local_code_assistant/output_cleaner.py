import re

def clean_output(text):

    # Remove markdown code blocks
    text = re.sub(r"```python", "", text)
    text = re.sub(r"```", "", text)

    # Keep only first code block-like section
    lines = []

    for line in text.splitlines():

        # Stop when explanation starts
        if (
            line.startswith("Reason:")
            or line.startswith("Explanation:")
            or line.startswith("# This code")
            or line.startswith("It's equivalent")
        ):
            break

        lines.append(line)

    return "\n".join(lines).strip()