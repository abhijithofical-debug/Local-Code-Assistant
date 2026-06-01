import requests

def ask_model(prompt):

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen2.5-coder",
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0,
                "num_predict": 200
            }
        }
    )

    text = response.json()["response"]

    # Remove markdown fences
    text = text.replace("```python", "")
    text = text.replace("```", "")

    return text.strip()