# coding: utf-8

import logging

from environs import Env

logging.basicConfig(level=logging.DEBUG)

env = Env()
env.read_env()

# llama
LLAMA_MODEL_NAME = env.str('LLAMA_MODEL_NAME', '')


# Redis
REDIS_DATABASE_URL = env.url('REDIS_DATABASE_URL', 'http://localhost')
REDIS_DATABASE_PORT = env.str('REDIS_DATABASE_PORT', '6379')