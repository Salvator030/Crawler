from sqlalchemy import Engine, select
from sqlalchemy.orm import Session

from Backend.Database import Database
from Backend.Orm.OrmInterfaces.ContentDaoInterface import ContentDaoInterface
from Backend.Orm.OrmModels.Content import Content


class ContentHandler(ContentDaoInterface):

    def __init__(self, database: Database):
        self.__database: Database = database
        self.__engine: Engine = database.engin

    def add_contents(self, contents:[Content]):
        with Session(self.__engine) as session:
            session.add_all(contents)

    def get_all_contents(self):
        with Session(self.__engine) as session:
            stm = select(Content).order_by(Content.id)
            return session.scalars(stm).all()

    def get_content_by_id(self, search_id:int):
        with Session(self.__engine) as session:
            stm = select(Content).where(Content.id == search_id)
            return session.scalars(stm).all()

    def get_contents_by_article(self, article_id):
        with Session(self.__engine) as session:
            stm = select(Content).where(Content.article_id == article_id)
            return session.scalars(stm).all()