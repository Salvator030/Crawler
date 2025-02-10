from Backend.Crawler.CrawlerInterface import CrawlerInterface
from Backend.Crawler.Parser.SpiegelParser import SpiegelParser
from Backend.Crawler.SpiegelCrawler import SpiegelCrawler
from Backend.Crawler.TspCrawler import TspCrawler
from Backend.Crawler.Fetcher import Fetcher
from Backend.Crawler.Parser import TspParser



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
