def fix_expected_colon(code):

    lines = code.split("\n")

    fixed = []

    for line in lines:

        stripped = line.strip()

        if (
            stripped.startswith("for ")
            or stripped.startswith("if ")
            or stripped.startswith("while ")
            or stripped.startswith("def ")
            or stripped.startswith("class ")
        ) and not stripped.endswith(":"):

            line += ":"

        fixed.append(line)

    return "\n".join(fixed)
