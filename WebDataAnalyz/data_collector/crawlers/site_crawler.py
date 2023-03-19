import scrapy

class SiteCrawler(scrapy.Spider):
    name = "site_crawler"

    starts_urls = [
        "https://www.python.org./blogs/",
    ]

    def parse(self, response):
        for article in response.css("article"):
            yield {
                "title": article.css("h2.entry-title a::text").get(),
                "date": article.css("time::attr(datetime)").get(),
            }
        next_page = response.css("a.next-posts-link::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)