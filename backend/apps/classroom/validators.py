from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy


def validate_negative(value: int):
    if value < 0:
        gettext_lazy(f"{value} is Not a Positive Number")
