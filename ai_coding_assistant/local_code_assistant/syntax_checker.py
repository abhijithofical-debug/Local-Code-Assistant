import ast

def check_syntax(code):

    try:
        ast.parse(code)

        return {
            "success": True,
            "message": "No syntax errors"
        }

    except SyntaxError as e:

        return {
            "success": False,
            "message": e.msg,
            "line": e.lineno
        }