from __future__ import absolute_import, unicode_literals

from celery import shared_task
import sys
import os
from django.core.management import call_command
from django.core import management
from django.core.management.commands import dumpdata
from datetime import datetime


@shared_task
def backup():
    now = datetime.now()
    timestamp = datetime.timestamp(now)

    if not os.path.isdir("./backups"):
        os.mkdir("./backups")

    with open("./backups/" + str(timestamp) + ".json", "w") as f:
        management.call_command("dumpdata", stdout=f)
