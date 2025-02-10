from abc import abstractmethod

from Backend.Orm.OrmModels.Content import Content


class ContentDaoInterface:

    @abstractmethod
    def add_contents(self, contents:[Content]):
        pass

    @abstractmethod
    def get_all_contents(self):
        pass

    @abstractmethod
    def get_content_by_id(self, search_id:int):
        pass

    @abstractmethod
    def get_contents_by_article(self, article_id):
        pass
