# coding: utf-8

from celery.app import Celery

from app import settings
from app.llama import LlamaModel


llama_model = LlamaModel(model_name=settings.LLAMA_MODEL_NAME)

broker_url = f'{settings.CELERY_BROKER_PROTOCOL}://{settings.CELERY_BROKER_URL}:{settings.CELERY_BROKER_PORT}'  # noqa: E501
app = Celery('tasks', broker=broker_url)


@app.task
def health() -> dict:
    return {'status': 'ok'}


@app.task
def predict(prompt: str, max_length: int, **kwargs) -> dict:
    predict = llama_model.predict(prompt=prompt, max_length=max_length)
    return {'status': 'ok', 'predict': predict}
