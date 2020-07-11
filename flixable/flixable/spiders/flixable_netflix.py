import scrapy


class NetflixList(scrapy.Spider):
    name = "netflix_list"
    start_urls = [
        'https://flixable.com/?min-rating=0&min-year=1920&max-year=2020&order=year#filterForm']

    def parse(self, response):
        titles = response.css("div.item")
        for title in titles:
            title_url = title.css(
                "div.card-body a::attr(href)").extract_first()
            title_name = title.css("h5.card-title::text").extract_first()
            title_id = title.css(
                "span.imdbRatingPlugin::attr(data-title)").extract_first()

            yield {
                'url': title_url,
                'name': title_name,
                'id': title_id
            }
