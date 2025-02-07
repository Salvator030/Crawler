from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship


from .Base import Base


class XPostInArticles(Base):
    __tablename__ = "xpost_in_articles"
    article_id: Mapped[int] = mapped_column(ForeignKey("article.id"), primary_key=True)
    xpost_id: Mapped[int] = mapped_column(ForeignKey("xpost.id"), primary_key=True)
    article: Mapped["Article"] =  relationship(back_populates="x_posts")
    xpost:  Mapped["XPost"] =  relationship(back_populates="articles")