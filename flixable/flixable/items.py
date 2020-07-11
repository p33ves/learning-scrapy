# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FlixableItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title_id = scrapy.Field()
    title_name = scrapy.Field()
    title_url = scrapy.Field()
