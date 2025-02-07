from Crawler.CrawlerInterface import CrawlerInterface
from Database import Database, DatabaseOption
from Orm.OrmHandler.ArticleHandler import ArticleHandler
from Orm.OrmModels import Article, Base


class OrmHandlerFactory:

    def __init__(self):
      self.__database = Database(DatabaseOption())

    def create_handler(self, type_of: type[Base]):
        if issubclass(type_of, Article):
            return ArticleHandler(self.__database)