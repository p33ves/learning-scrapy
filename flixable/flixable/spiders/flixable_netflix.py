import scrapy
from ..items import FlixableItem


class NetflixList(scrapy.Spider):
    name = "netflix_list"
    api_url = 'https://flixable.com/pagination2.php?min-rating=0&min-year=1920&max-year=2020&order=title&originals=0&page={}'
    start_urls = [
        "https://flixable.com/?min-rating=0&min-year=1920&max-year=2020&order=title#filterForm"]
    page_num = 1

    def parse(self, response):
        if response.status == 200:
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
            self.page_num = self.page_num + 1
            # yield scrapy.Request(url=self.api_url.format(next_page), callback=self.parse)
            yield response.follow(url=self.api_url.format(self.page_num), callback=self.parse)
