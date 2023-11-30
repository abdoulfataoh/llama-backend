# coding: utf-8

from app import settings
from app.llama import LlamaModel

__all__ = [
    'llama_model',
]

llama_model = LlamaModel(model_name=settings.LLAMA_MODEL_NAME)
