import datetime
import re

import scrapy
from us_fuels.enums import Fuels
from get_prices_scrapy.items import PricesItem


class CstoredecisionsSpider(scrapy.Spider):
    name = "cstoredecisions"
    allowed_domains = ["cstoredecisions.com"]
    start_urls = ["https://cstoredecisions.com/rack-prices/?city=orlando-fl"]

    def parse(self, response):
        security_code = re.findall('"rack_prices_nonce":"(\w+)"', response.text)[0]
        city_option = response.xpath('//*[@id="rack-price-city"]/option/@value').getall()
        city_name = response.xpath('//*[@id="rack-price-city"]').css('option::text').getall()
        city_dict = dict(zip(city_name, city_option))
        for city_name, city_slug in city_dict.items():
            for fuel in Fuels:
                url = f"https://cstoredecisions.com/wp-admin/admin-ajax.php?action=get_rack_prices&security={security_code}&type={fuel.value}&city={city_slug}"
                yield response.follow(url,
                                      callback=self.parse_fuel,
                                      meta={'city_name': city_name,
                                            'fuel': fuel,
                                            'city_slug': city_slug})

    def parse_fuel(self, response):
        data = response.json()
        posix_date = int(str(data[-1][0])[:-3])
        date = datetime.datetime.fromtimestamp(posix_date)
        price = data[-1][1]
        item = PricesItem()
        item['city_slug'] = response.meta.get('city_slug')
        item['date'] = date
        item['price'] = price
        item['fuel'] = response.meta.get('fuel')
        yield item