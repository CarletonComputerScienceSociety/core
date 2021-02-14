from __future__ import absolute_import, unicode_literals

from celery import shared_task
import sys
from django.core.management import call_command
from django.core import management
from django.core.management.commands import dumpdata

@shared_task
def backup():
    print("backup - shared task")
    with open('./backup.json', 'w') as f:
        management.call_command('dumpdata', stdout=f)