import click as click
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor


@click.command()
@click.option('--config', default='conf')
def explorer_start():
    settings = get_project_settings()
    configure_logging(settings)
    runner = CrawlerRunner()
    runner.crawl(s)
    defer = runner.join()
    defer.addBoth(lambda _: reactor.stop())
    reactor.run()