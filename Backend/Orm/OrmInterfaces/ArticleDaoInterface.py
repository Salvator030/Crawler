from abc import abstractmethod

from Backend.Orm.OrmModels import Article


class ArticleDaoInterface:

    @abstractmethod
    def get_all_articles(self) -> []:
         pass
    #
    # def get_last_articles(self) -> []:
    #     pass
    #
    @abstractmethod
    def get_article_by_id(self, search_id: int) -> []:
         pass

    @abstractmethod
    def get_article_by_headline(self, search_headline:str):
        pass

    # def get_article_by_date(self) -> []:
    #     pass
    #
    # def get_article_by_writer(self) -> []:
    #     pass
    #
    # def get_article_by_publisher(self) -> []:
    #     pass
    #
    # def get_article_by_date_and_writer(self) -> []:
    #     pass

    @abstractmethod
    def add_articles(self, articles:[Article]):
        pass