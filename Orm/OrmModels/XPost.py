from typing import List

from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship


from .Base import Base
from .XPostsInArticles import XPostInArticles


class XPost(Base):
    __tablename__ = "xpost"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    articles: Mapped[List["XPostInArticles"]] = relationship(back_populates="xpost")
