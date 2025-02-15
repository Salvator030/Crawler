import threading
from threading import Thread

from Backend.Crawler.MainCrawler import MainCrawler
from Backend.Orm.OrmHandler import ArticleHandler, OrmHandlerFactory
from Backend.Orm.OrmModels.Article import Article


class CrawlAndPersistArticlesThread(Thread):
    def __init__(self):
        super().__init__()
        self.__main_crawler: MainCrawler = MainCrawler()
        self.__article_handler: ArticleHandler = OrmHandlerFactory().create_handler(Article)
        self._stop_event = threading.Event()

    def run(self):
        while not self._stop_event.is_set():
            for crawler in self.__main_crawler.crawlers.values():
                articles: list[Article] = crawler.crawl_articles()
                if articles:
                    print(f"Articles to add: {articles}")
                self.__article_handler.add_articles(articles)
                if self._stop_event.is_set():
                    break

    def stop(self):
        self._stop_event.set()



