from django.db import models
from django.utils.translation import gettext_lazy as _


class Fuels(models.TextChoices):
    diesel = 1, _('Diesel')
    unleaded_regular = 2, _('Unleaded Regular')
    undeaded_mid_grade = 3, _('Undeaded Mid-Grade')
    unleaded_premium = 4, _('Unleaded Premium')
