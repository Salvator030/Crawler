from Backend.Crawler.CrawlerInterface import CrawlerInterface
from Backend.Crawler.Fetcher import Fetcher

from Backend.Crawler.Interactor.TspInteractor import TspInteractor
from Backend.Crawler.Parser import ParserInterface
from Backend.Orm.OrmModels import Article


class TspCrawler(CrawlerInterface):

    def __init__(self, fetcher: Fetcher, parser: ParserInterface):
        self.__fetcher = fetcher
        self.__parser = parser
        self._tsp_url = "https://www.tagesspiegel.de/schlagzeilen/"



    def __crawl_main_page(self):
        main_page_dom =  self.__parser.parse_requests(self.__fetcher.fetch(self._tsp_url))
        articles_urls =  self.__parser.get_free_articles_urls(main_page_dom)
        return articles_urls

    def crawl_article(self, url: str):
        interactor = TspInteractor()
        article_dom = self.__parser.parse_requests(self.__fetcher.fetch(url))
        article = self.__parser.parse_article(article_dom)
        if article is not None:
            article.url = url
            article.x_posts = [] #interactor.search_for_x_posts(url)
        return article

    def crawl_articles(self):

        articles_urls = self.__crawl_main_page()
        articles = [Article]
        for url in articles_urls:
            article = self.crawl_article(url)
            if article is not None:
                articles.append(article)
        return articles


