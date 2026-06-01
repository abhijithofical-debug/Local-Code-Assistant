from setuptools import setup, find_packages

setup(
    name="local-code-assistant",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    author="Abhijith",
    description="Local AI Coding Assistant using Ollama",
    python_requires=">=3.8",
)