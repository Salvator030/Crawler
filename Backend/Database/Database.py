from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from . import DatabaseOption
from Backend.Orm.OrmModels.Base import Base
from Backend.Orm.OrmModels.Article import Article


class Database:

    def __init__(self,db_option:DatabaseOption):
      self.db_option: DatabaseOption = db_option
      self.engin = self.__connect()

    def __connect(self):
        engine_str = f"mysql+mysqlconnector://{self.db_option.user}:{self.db_option.pwd}@{self.db_option.host}/{self.db_option.db_Name}?charset=utf8mb4"
        print(engine_str)
        engine = create_engine(engine_str, echo=True)
        Base.metadata.create_all(bind=engine)
        return engine


