import scrapy
from scrapy.crawler import CrawlerProcess


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['www.fitmedia.net']
    start_urls = ['https://www.fitmedia.net/']

    def parse(self, response):
        yield response

def main():
    process = CrawlerProcess()
    process.crawl(TestSpider)
    process.start()
