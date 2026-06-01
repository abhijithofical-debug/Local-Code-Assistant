# Local-Code-Assistant

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

Download Ollama:

https://ollama.com

Download the model:

ollama pull qwen2.5-coder

## Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/Local-Code-Assistant.git

cd Local-Code-Assistant

Install dependencies:

pip install -r requirements.txt

## Example

from local_code_assistant import Assistant

ai = Assistant()

print(
ai.generate_code(
"Create a Python prime checker"
)
)
