from sqlalchemy import Integer, ForeignKey, Text
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .Base import Base

class Content(Base):
    __tablename__ = "content"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    article_id: Mapped[int] = mapped_column(ForeignKey("article.id"))
    text: Mapped[str] = mapped_column(Text(), nullable=False)
    article: Mapped["Article"] = relationship(back_populates="contents", single_parent=True,
        cascade="all, delete-orphan")
    date: Mapped[DATETIME] = mapped_column(DATETIME,nullable=False)

    def __repr__(self) -> str:
        return f"content(id={self.id!r},\narticle_id={self.article_id!r},\ntext={self.text!r},\narticle={self.article!r})"
