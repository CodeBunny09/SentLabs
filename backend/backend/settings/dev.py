# backend/settings/dev.py

from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Additional development settings can be added here
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
