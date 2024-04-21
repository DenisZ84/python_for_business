from enum import Enum

from django.db.models import Func, Value, CharField, When, Case, F
from django.db.models.lookups import Exact


def get_enum_value(field_name: F, val: Enum):
    return Case(*[When(Exact(field_name, choice.value), then=Value(choice.label, output_field=CharField())) for choice in val])


class TimestampToIST(Func):

    function = 'timezone'
    template = "%(function)s('Europe/Moscow', %(expressions)s)"


class TimestampToStr(Func):

    function = 'to_char'
    template = "%(function)s(%(expressions)s, 'DD.MM.YY')"
    output_field = CharField()