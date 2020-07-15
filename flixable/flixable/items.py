# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FlixableListItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title_id = scrapy.Field()
    title_name = scrapy.Field()
    title_url = scrapy.Field()


class NetflixItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title_id = scrapy.Field()
    title_name = scrapy.Field()
    title_url = scrapy.Field()
    description = scrapy.Field()
    release_year = scrapy.Field()
    title_certification = scrapy.Field()
    length = scrapy.Field()
    cast = scrapy.Field()
    production_country = scrapy.Field()
    added_date = scrapy.Field()
    imdb_rating = scrapy.Field()
