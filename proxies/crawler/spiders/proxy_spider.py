from scrapy import Spider

from proxies.crawler.model.crawler_task import ProxyCrawlerTask


class ProxySpider(Spider):
    def __init__(self, task: ProxyCrawlerTask, **kwargs):
        super().__init__(**kwargs)
        self.__task = task

    def parse(self, response, **kwargs):
        items = self.__task.locator.get_ip_ports(response)
        for item in items:
            yield item

