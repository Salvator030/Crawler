from abc import abstractmethod

from Backend.Crawler.Fetcher import Fetcher
from Backend.Crawler.Parser import ParserInterface


class CrawlerInterface:

    @abstractmethod
    def __init__(self, fetcher: Fetcher, parser: ParserInterface):
        pass

    @abstractmethod
    def __crawl_main_page(self):
        pass

    @abstractmethod
    def crawl_article(self, url: str):
        pass

    @abstractmethod
    def crawl_articles(self):
        pass
