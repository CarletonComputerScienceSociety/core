from .base import *

from django.core.management.utils import get_random_secret_key

if os.environ.get("GITHUB_WORKFLOW"):
    SECRET_KEY = get_random_secret_key()

DEBUG = True
