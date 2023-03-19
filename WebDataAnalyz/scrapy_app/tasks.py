from celery import shared_task
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from .scrapy_project.scrapy_project.spiders.example_spider import ExampleSpider

@shared_task
def run_example_spider():
    process = CrawlerProcess(get_project_settings())
    process.crawl(ExampleSpider)
    process.start()
