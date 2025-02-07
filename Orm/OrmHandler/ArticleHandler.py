from datetime import datetime
from warnings import catch_warnings

from django.db.models.fields import return_None
from sqlalchemy import Engine, select, Executable, Result
from sqlalchemy.orm import Session, joinedload

from Database import Database
from Orm.OrmInterfaces.ArticleDaoInterface import ArticleDaoInterface
from Orm.OrmModels import Article, Content

from sqlalchemy.orm import joinedload

class ArticleHandler(ArticleDaoInterface):
    def __init__(self, database: Database):
        self.__database: Database = database
        self.__engine: Engine = database.engin

    from datetime import datetime

    from datetime import datetime

    from datetime import datetime

    def add_articles(self, articles: list[Article]):
        print(f"add_articles")
        with Session(self.__engine) as session:

                for article in articles:
                    # check if article in database
                    print(article)
                    stm = select(Article).where(Article.headline == article.headline)
                    result = session.scalars(stm).first()
                    print("res " + str(result))
                    if result is None:
                        # if not add article

                        session.add(article)
                    else:
                        # Ensure the current_date and new_date are actual datetime objects
                        current_date = result.data
                        new_date = article.data

                        # Print the values to verify
                        print(f"Current date: {current_date} (Type: {type(current_date)})")
                        print(f"New date: {new_date} (Type: {type(new_date)})")

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

    def get_article_by_id(self, search_id: int):
        with Session(self.__engine) as session:
            stm = select(Article).options(joinedload(Article.contents).joinedload(Content.article)).where(Article.id == search_id)
            return session.scalars(stm).unique().all()

    def get_article_by_headline(self, search_headline: str):
        with Session(self.__engine) as session:
            stm = select(Article).options(joinedload(Article.contents).joinedload(Content.article)).where(Article.headline == search_headline)
            return session.scalars(stm).unique()


