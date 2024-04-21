from django.db import models

from us_fuels.enums import Fuels


class USCity(models.Model):
    """Города США."""
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    lat = models.FloatField()
    lon = models.FloatField()


class UsFuel(models.Model):
    """Данные по топливу по городам США."""
    city_slug = models.SlugField()
    date = models.DateField()
    price = models.FloatField()
    fuel = models.CharField(max_length=2, choices=Fuels)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.fuel

