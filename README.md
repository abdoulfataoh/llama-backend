<p align="center">
    <img src="docs/icon.png" alt="icon">
    <br>Llama-backend<br>
</p>


Llama-backend is a scalable and reliable backend service that provides a robust API for managing requests to the llama model. It is designed to be easy to use and integrate with existing applications, and it is built on top of modern technologies such as FastAPI and Celery.

### Requirements

We use [poetry](https://python-poetry.org/) in this project to manage virtual env and dependancies. To install poetry, run the follwing command

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Before using llama model, you must:
- Request access by filling this [form](https://ai.meta.com/resources/models-and-libraries/llama-downloads/)


- Request access on meta [huggingface page](https://huggingface.co/meta-llama)

### Installation

Install the project dependancies

```bash
poetry install
```

HuggingFace login

```bash
huggingface-cli login --token <YOUR_ACCESS_TOKEN>
```

### Usage

Start the start with unicorn

```bash
uvicorn start:fastapi_app --reload
```
  