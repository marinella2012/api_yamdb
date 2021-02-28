from datetime import date

from django.core.exceptions import ValidationError


def no_future(value):
    today = date.today().year
    if value > today:
        raise ValidationError('Year cannot be in the future.')
