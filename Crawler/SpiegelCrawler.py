from datetime import datetime

from Crawler.CrawlerInterface import CrawlerInterface
from Fetcher import Fetcher
from Interactor.TspInteractor import TspInteractor
from Orm.OrmModels import Article
from Parser.ParserInterface import ParserInterface


class SpiegelCrawler(CrawlerInterface):

    def __init__(self, fetcher: Fetcher, parser: ParserInterface):
        self.__fetcher = fetcher
        self.__parser = parser
        self._spiegel_url = "https://www.spiegel.de/schlagzeilen/"

    def __crawl_main_page(self):
        main_page_dom = self.__parser.parse_requests(self.__fetcher.fetch(self._spiegel_url))
        articles_urls = self.__parser.get_free_articles_urls(main_page_dom)
        print("articles_urls leg: " + str(len(articles_urls)))
        return articles_urls

    def crawl_article(self, url: str) -> Article:
        print("url: " + url)
        interactor = TspInteractor()
        article_dom = self.__parser.parse_requests(self.__fetcher.fetch(url))
        article = self.__parser.parse_article(article_dom)
        if article is not None:
            article.url = url
            article.x_posts = []  # interactor.search_for_x_posts(url)
        return article

    def crawl_articles(self) -> list[Article]:
        articles_urls = self.__crawl_main_page()
        articles = [Article]
        for url in articles_urls:
            article = self.crawl_article(url)
            if  article is not None:
                articles.append(article)
        print("articles leg: " + str(len(articles)))
        return articles
