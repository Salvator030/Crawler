from Backend.Database import Database, DatabaseOption
from Backend.Orm.OrmHandler.ArticleHandler import ArticleHandler
from Backend.Orm.OrmModels.Article import Article
from Backend.Orm.OrmModels.Base import Base


class OrmHandlerFactory:

    def __init__(self):
      self.__database = Database(DatabaseOption())

    def create_handler(self, type_of: type[Base]):
        if issubclass(type_of, Article):
            return ArticleHandler(self.__database)