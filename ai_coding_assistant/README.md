# Local Code Assistant

A local AI-powered coding assistant built using Python and Ollama.

## Features

* Syntax Error Detection
* Syntax Error Fixing
* Runtime Error Detection
* Runtime Error Fixing
* Code Completion
* Code Review
* Code Explanation
* Code Generation
* Documentation Generation
* Alternative Code Suggestions

## Requirements

* Python 3.8+
* Ollama

## Install Ollama

Download and install Ollama:

https://ollama.com

Pull a coding model:

```bash
ollama pull qwen2.5-coder
```

or

```bash
ollama pull deepseek-coder
```

Start Ollama:

```bash
ollama serve
```

## Installation

```bash
pip install local-code-assistant
```

## Example

```python
from local_code_assistant import Assistant

ai = Assistant()

print(
    ai.generate_code(
        "Create a Python prime checker"
    )
)
```
