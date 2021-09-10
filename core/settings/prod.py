from django.core.management.utils import get_random_secret_key
from sentry_sdk.integrations.django import DjangoIntegration
import sentry_sdk
import environ

from .base import *
SECRET_KEY = get_random_secret_key()

DEBUG = False


ALLOWED_HOSTS = ["core.carletoncomputerscience.ca", "localhost"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "code-project",
        "USER": "postgres",
        "PASSWORD": "1234",
        "HOST": "localhost",
        "PORT": 5432,
    }
}

sentry_sdk.init(
    dsn="https://8f90d41a491540b6a02909ac87aa0c18@o990880.ingest.sentry.io/5953309",
    integrations=[DjangoIntegration()],
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,
)
