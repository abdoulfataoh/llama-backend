# coding: utf-8

import logging

from environs import Env

logging.basicConfig(level=logging.DEBUG)

env = Env()
env.read_env()

# llama
LLAMA_MODEL_NAME = env.str('LLAMA_MODEL_NAME', '')

# Redis
CELERY_BROKER_PROTOCOL = env.str('CELERY_BROKER_PROTOCOL', 'redis')
CELERY_BROKER_URL = env.str('REDIS_DATABASE_URL', 'localhost')
CELERY_BROKER_PORT = env.str('REDIS_DATABASE_PORT', '6379')
CELERY_BROKER_PASSWORD = env.str('CELERY_BROKER_PASSWORD', '')
