from threading import Event

from Backend.Crawler.CrawlerFactory import CrawlerFactory
from Backend.Crawler.CrawlerInterface import CrawlerInterface
from Backend.Crawler.SpiegelCrawler import SpiegelCrawler
from Backend.Crawler.TspCrawler import TspCrawler
from Backend.Orm.OrmHandler import OrmHandlerFactory
from Backend.Orm.OrmModels import Article


class MainCrawler:

    def __init__(self):
        self.__crawler_factory = CrawlerFactory()
        self.crawlers: [CrawlerInterface] = self.__init_crawlers()
        self.__article_handler = self.__init_handler()

    def __init_crawlers(self):
        crawler_types = [TspCrawler, SpiegelCrawler]
        crawlers = {crawler.__name__: self.__crawler_factory.create_crawler(crawler) for crawler in crawler_types}
        return crawlers

    @staticmethod
    def __init_handler():
        handler_factory = OrmHandlerFactory()
        return handler_factory.create_handler(Article)




