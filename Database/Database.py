from sqlalchemy import create_engine, Engine, select
from sqlalchemy.orm import Session, DeclarativeMeta

from . import DatabaseOption
from Orm.OrmModels import Base, Article


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

    def add(self,models: [Base]):
        with Session(self.engin) as session:
            session.add_all(models)
            session.commit()


    def get_all(self, model_class: type[Base]):
        with Session(self.engin) as session:
            stm= select(model_class).order_by(Article.id)
            return session.scalars(stm).all()

    def get_all_by(self,model_class: type[Base], identifier: str ):
        with Session(self.engin) as session:
            stm= select(model_class).order_by(Article.id)
            return session.scalars(stm).all()

