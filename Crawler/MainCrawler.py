from Crawler.CrawlerFactory import CrawlerFactory
from Crawler.CrawlerInterface import CrawlerInterface
from Crawler.SpiegelCrawler import SpiegelCrawler
from Crawler.TspCrawler import TspCrawler
from Orm.OrmHandler import OrmHandlerFactory
from Orm.OrmModels import Content, Article


class MainCrawler:

    def __init__(self):
        self.__crawler_factory = CrawlerFactory()
        self.__crawlers: [CrawlerInterface] = self.__init_crawlers()
        self.__article_handler = self.__init_handler()

    def __init_crawlers(self):
        crawler_types = [TspCrawler, SpiegelCrawler]
        crawlers = {crawler.__name__: self.__crawler_factory.create_crawler(crawler) for crawler in crawler_types}
        return crawlers

    def __init_handler(self):
        handler_factory = OrmHandlerFactory()
        return handler_factory.create_handler(Article)

    def crawl_all_news_papers(self):
        for crawler in self.__crawlers.values():
            articles = crawler.crawl_articles()
            self.__article_handler.add_articles(articles)

    def crawl_tagesspiegel(self):
        return self.__crawlers.get("TspCrawler").crawl_articles()

    def crawl_spiegel(self):
        return self.__crawlers.get("SpiegelCrawler").crawl_articles()
