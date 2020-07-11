import scrapy
from ..items import FlixableItem


class NetflixList(scrapy.Spider):
    name = "netflix_list"
    start_urls = [
        'https://flixable.com/?min-rating=0&min-year=1920&max-year=2020&order=year#filterForm']

    def parse(self, response):
        titles = response.css("div.item")
        item = FlixableItem()
        for title in titles:
            item['title_url'] = title.css(
                "div.card-body a::attr(href)").extract_first()
            item['title_name'] = title.css(
                "h5.card-title::text").extract_first()
            item['title_id'] = title.css(
                "span.imdbRatingPlugin::attr(data-title)").extract_first()
            yield item
