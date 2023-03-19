from django.http import JsonResponse
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from .crawlers.site_crawler import SiteCrawler
from .tasks import run_crawler_task

def run_crawler(request):
    run_crawler_task.delay()

    # the results return in a json format
    return JsonResponse({"message": "Crawler has been started"})