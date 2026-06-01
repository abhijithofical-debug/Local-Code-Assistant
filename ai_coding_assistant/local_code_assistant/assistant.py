from .syntax_checker import check_syntax
from .rule_fixer import fix_expected_colon
from .fixer import fix_code
from .completion import complete_code
from .reviewer import review_code
from .docs_generator import generate_docs
from .ai_docs import generate_ai_docs
from .runtime_checker import check_runtime
from .runtime_explainer import explain_runtime_error
from .runtime_fixer import fix_runtime_error
from .code_explainer import explain_code
from .alternatives import suggest_alternatives
from .code_generator import generate_code

class Assistant:

    def explain_error(self, code):

        return check_syntax(code)

    def fix_error(self, code):

        result = check_syntax(code)

        if result["success"]:
            return code

        if result["message"] == "expected ':'":
            return fix_expected_colon(code)

        return fix_code(
            code,
            result["message"]
        )

    def complete(self, code):

        result = complete_code(code)

        if result:
            return result

        return "No suggestion available"

    def review_code(self, code):

        return review_code(code)

    def generate_docs(self, code):

        return generate_docs(code)

    def generate_ai_docs(self, code):

        return generate_ai_docs(code)

    def check_runtime(self, code):

        return check_runtime(code)

    def explain_runtime_error(self, code):

        return explain_runtime_error(code)

    def fix_runtime_error(self, code):

        return fix_runtime_error(code)

    def explain_code(self, code):

        return explain_code(code)

    def suggest_alternatives(self, code):

        return suggest_alternatives(code)
    def generate_code(self, prompt):

        return generate_code(prompt)