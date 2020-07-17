import json
import scrapy
from ..items import FlixableNetflixItem


class NetflixItem(scrapy.Spider):
    name = "netflix_item"
    base_url = "https://flixable.com"
    list_file = open("data/netflix_list.json")
    list_data = json.load(list_file)
    # [self.base_url+row['title_url'] for row in list_data] -----> why doesn't this work?
    start_urls = list()
    for row in list_data:
        start_urls.append(base_url+row['title_url'])

    def parse(self, response):
        data = response.css("div.section-sections")
        item = FlixableNetflixItem()
        item['title_name'] = data.css("h1.title::text").extract_first()
        item['release_year'], item['title_certification'], item['length'] = data.css(
            "h6.card-category").css("span::text").extract()
        item['description'] = data.css(
            "p.card-description::text").extract_first()
        for para in data.css("p"):
            if para.css("span.mr-2::text").extract_first() == 'Genres:':
                item['genre'] = para.css("a::text").extract()
            elif para.css("span.mr-2::text").extract_first() == 'Cast:':
                item['cast'] = para.css("a::text").extract()
            elif para.css("span.mr-2::text").extract_first() == 'Production Country:':
                item['production_country'] = para.css("a::text").extract()
            elif para.css("span.mr-2::text").extract_first() == '\n                    Added to Netflix:':
                item['added_date'] = para.css("span::text")[1].extract()
        yield item


"""         elif para.css("span.imdbRatingPlugin"):
                item['imdb_rating'] = para.css(
                    "span.imdbRatingPlugin").css("span.rating::text")
"""
