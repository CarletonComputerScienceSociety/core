from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

import re


def validate_carleton_email(value):
    search = re.findall("(cmail|cunet)\.carleton\.ca", value)
    if len(search) != 1:
        raise ValidationError(
            _("Invalid email domain, must be carleton.ca email."), status="invalid"
        )
