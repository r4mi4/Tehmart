# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TehmartItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    price_before_discount = scrapy.Field()
    image_link = scrapy.Field()
    page_link = scrapy.Field()
    description = scrapy.Field()
    specifications = scrapy.Field()

