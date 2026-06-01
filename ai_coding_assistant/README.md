# Local Code Assistant

A local AI-powered coding assistant built using Python and Ollama.

## Features

- Syntax Error Detection
- Syntax Error Fixing
- Runtime Error Detection
- Runtime Error Fixing
- Code Completion
- Code Review
- Code Explanation
- Code Generation
- Documentation Generation
- Alternative Code Suggestions

## Installation

pip install local-code-assistant

## Example

from local_code_assistant import Assistant

ai = Assistant()

print(
    ai.generate_code(
        "Create a Python prime checker"
    )
)