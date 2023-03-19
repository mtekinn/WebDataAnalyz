from celery import shared_task
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from .crawlers.site_crawler import SiteCrawler


@shared_task
def run_crawler_task():
    process = CrawlerProcess(get_project_settings())
    process.crawl(SiteCrawler)
    process.start()