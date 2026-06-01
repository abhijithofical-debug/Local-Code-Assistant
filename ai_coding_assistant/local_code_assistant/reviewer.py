def review_code(code):

    suggestions = []

    if "print(" in code and code.count("print(") > 5:
        suggestions.append(
            "Too many print statements detected."
        )

    if "while True" in code:
        suggestions.append(
            "Infinite loop detected. Ensure exit condition exists."
        )

    if not suggestions:
        suggestions.append(
            "No issues found."
        )

    return suggestions