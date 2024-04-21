
from scrapy_djangoitem import DjangoItem
from us_fuels.models import UsFuel


class PricesItem(DjangoItem):
    django_model = UsFuel
