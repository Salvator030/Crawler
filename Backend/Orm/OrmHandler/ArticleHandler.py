from datetime import datetime

from sqlalchemy import Engine, select, or_, Date, cast
from sqlalchemy.orm import Session

from Backend.Database import Database
from Backend.Orm.OrmInterfaces.ArticleDaoInterface import ArticleDaoInterface
from Backend.Orm.OrmModels import Article, Content

from sqlalchemy.orm import joinedload
from datetime import datetime

class ArticleHandler(ArticleDaoInterface):
    def __init__(self, database: Database):
        self.__database: Database = database
        self.__engine: Engine = database.engin

    def add_articles(self, articles: list[Article]):
        with Session(self.__engine) as session:

                for article in articles:
                    # check if article in database
                    stm = select(Article).where(Article.headline == article.headline)
                    result = session.scalars(stm).first()

                    if result is None:
                        # if not add article

                        session.add(article)
                    else:
                        # Ensure the current_date and new_date are actual datetime objects
                        current_date = result.data
                        new_date = article.data

                        # Convert to datetime objects if necessary
                        if isinstance(current_date, datetime) and isinstance(new_date, datetime):
                            # Convert to offset-naive datetime if necessary
                            if current_date.tzinfo is not None:
                                current_date = current_date.replace(tzinfo=None)
                            if new_date.tzinfo is not None:
                                new_date = new_date.replace(tzinfo=None)

                            # if article in database and date < crawled article.date update database
                            if current_date < new_date:
                                result.contents.append(article.contents[0])
                                result.data = new_date
                session.commit()


    def get_all_articles(self):
        with Session(self.__engine) as session:
            stm = select(Article).options(joinedload(Article.contents).joinedload(Content.article)).order_by(Article.id)
            return session.scalars(stm).unique().all()


    def get_article_by(self,json):
        publishers = [string.upper() for string in json["publisher"] ]


        stm = None
        result = None
        if json['date'] != "":
            date = datetime.strptime(json['date'], '%Y-%m-%d')
            if len(publishers) > 0:
                stm = select(Article).options(joinedload(Article.contents).joinedload(Content.article)).where(
                    Article.publisher.in_(publishers), cast(Article.data, Date) == date)
            else:
                stm = select(Article).options(joinedload(Article.contents).joinedload(Content.article)).where(
                    cast(Article.data, Date) == date)

        else:
            stm = select(Article).options(joinedload(Article.contents).joinedload(Content.article)).where(Article.publisher.in_(publishers))

        with Session(self.__engine) as session:
            res = session.scalars(stm).unique().all()
            print(len(res))
            return res


    def get_article_by_id(self, search_id: int):
        with Session(self.__engine) as session:
            stm = select(Article).options(joinedload(Article.contents).joinedload(Content.article)).where(Article.id == search_id)
            return session.scalars(stm).unique().all()

    def get_article_by_headline(self, search_headline: str):
        with Session(self.__engine) as session:
            stm = select(Article).options(joinedload(Article.contents).joinedload(Content.article)).where(Article.headline == search_headline)
            return session.scalars(stm).unique()


