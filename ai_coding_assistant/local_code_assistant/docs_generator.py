import re

def generate_docs(code):

    match = re.search(
        r"def\s+(\w+)\((.*?)\):",
        code
    )

    if not match:
        return "No function found."

    func_name = match.group(1)

    params = [
        p.strip()
        for p in match.group(2).split(",")
        if p.strip()
    ]

    doc = f'"""\n{func_name} function.\n\nArgs:\n'

    for param in params:
        doc += f"    {param}: Description\n"

    doc += '\nReturns:\n    Description\n"""'

    return doc