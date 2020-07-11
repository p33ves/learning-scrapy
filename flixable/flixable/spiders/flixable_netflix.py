import scrapy


class NetflixList(scrapy.Spider):
    name = "netflix_list"
    start_urls = [
        'https://flixable.com/?min-rating=0&min-year=1920&max-year=2020&order=year#filterForm']

    def parse(self, response):
        pass
