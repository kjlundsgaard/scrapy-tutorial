import scrapy

from stackoverflow.items import StackOverflowItem


class MySpider(scrapy.Spider):
    name = "stackoverflow"
    allowed_domains = ["http://stackoverflow.com"]
    start_urls = ["http://stackoverflow.com/"]

    def parse(self, response):
        for sel in response.xpath("//div[@class='summary']/h3"):
            item = StackOverflowItem()
            item['title'] = sel.xpath("a/text()").extract()
            item['link'] = sel.xpath("a/@href").extract()
            yield item
