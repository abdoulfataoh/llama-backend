# coding: utf-8

from typing import Any

import transformers
import torch


__all__ = [
    'LlamaModel',
]


class LlamaModel:

    _tokenizer: transformers.PreTrainedTokenizer
    _pipeline: transformers.Pipeline
    _model: Any

    def __init__(self, model_name: str) -> None:
        self._tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)  # noqa: E501
        self._pipeline = transformers.pipeline(
           "text-generation",
           model=model_name,
           torch_dtype=torch.float16,
           device_map="auto",
        )

    def predict(self, prompt: str, max_length: int = 200, **kwargs) -> str:
        sequences = self._pipeline(
            prompt,
            do_sample=True,
            max_length=max_length,
            top_k=10,
            num_return_sequences=1,
            eos_token_id=self._tokenizer.eos_token_id,
        )

        output: str = ''
        for seq in sequences:
            output += seq['generated_text']

        return output
