# coding: utf-8

from fastapi import FastAPI

from app import tasks

__all__ = [
    'fastapi_app',
]


fastapi_app = FastAPI()


@fastapi_app.get("/health/")
async def health():
    task = tasks.health.delay()
    return {"task_id": task.id}


@fastapi_app.post("/predict/")
async def predict(prompt: str, max_length: int):
    task = tasks.predict.delay()
    return {"task_id": task.id}
