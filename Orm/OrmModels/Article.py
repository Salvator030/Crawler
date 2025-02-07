from typing import List
from sqlalchemy import String, Integer, Text, ForeignKey
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .Base import Base
from .Content import Content

class Article(Base):
    __tablename__ = "article"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    data: Mapped[DATETIME] = mapped_column(DATETIME, nullable=False)
    headline: Mapped[str] = mapped_column(Text(), nullable=False)
    sub_headline: Mapped[str] = mapped_column(Text(), nullable=False)
    description: Mapped[str] = mapped_column(Text(), nullable=False)
    contents: Mapped[List["Content"]] = relationship(back_populates="article")
    writer: Mapped[str] = mapped_column(String(150), nullable=False)
    publisher: Mapped[str] = mapped_column(String(50), nullable=False)
    url: Mapped[str] = mapped_column(Text(), nullable=False)
    x_posts: Mapped[List["XPostInArticles"]] = relationship(back_populates="article")

    def __repr__(self) -> str:
        return (f"article(id={self.id!r}, data={self.data!r}, headline={self.headline!r}, "
                f"sub_headline={self.sub_headline!r}, description={self.description!r}, "
                f"contents={self.contents!r}, writer={self.writer!r}, publisher={self.publisher!r}, url={self.url!r})")
