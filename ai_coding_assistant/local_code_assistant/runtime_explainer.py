from .runtime_checker import check_runtime


def explain_runtime_error(code):

    result = check_runtime(code)

    if result["success"]:
        return "No runtime errors found."

    error = result["error_type"]

    if error == "NameError":
        return f"""
Runtime Error: NameError

{result['message']}

Possible Fix:
Define the variable before using it.
"""

    elif error == "ZeroDivisionError":
        return f"""
Runtime Error: ZeroDivisionError

{result['message']}

Possible Fix:
Check if denominator is zero before division.
"""

    elif error == "IndexError":
        return f"""
Runtime Error: IndexError

{result['message']}

Possible Fix:
Ensure index exists in the list.
"""

    return f"""
Runtime Error: {error}

{result['message']}
"""