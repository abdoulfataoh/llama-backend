# coding: utf-8

from celery.app import Celery

from app import settings

broker_url =  f'{settings.CELERY_BROKER_PROTOCOL}://{settings.CELERY_BROKER_URL}:{settings.CELERY_BROKER_PORT}' # noqa: F401

app = Celery(__name__, broker=broker_url)


@app.task
def health() -> dict:
    return {'status': 'ok'}