from Crawler.CrawlerInterface import CrawlerInterface
from Crawler.SpiegelCrawler import SpiegelCrawler
from Crawler.TspCrawler import TspCrawler
from Fetcher import Fetcher
from Parser import TspParser
from Parser.SpiegelParser import SpiegelParser


class CrawlerFactory:

    def __init__(self):
        self.__fetcher = Fetcher()

    def create_crawler(self, type_of: type[CrawlerInterface]) -> CrawlerInterface:

        if issubclass(type_of, TspCrawler):
            parser = TspParser()
            return TspCrawler(self.__fetcher,parser)
        elif issubclass(type_of, SpiegelCrawler):
            parser = SpiegelParser()
            return SpiegelCrawler(self.__fetcher,parser)
        else:
            raise ValueError(f"Unbekannter Crawler-Typ: {type_of}")
