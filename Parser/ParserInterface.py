from datetime import datetime

from bs4 import BeautifulSoup

from Orm.OrmModels import Article


class ParserInterface:


    def parse_requests(self, res) -> BeautifulSoup:
        pass

    def get_free_articles_urls(self, res) -> []:
        pass

    def get_article_header(self, dom) -> []:
        pass

    def get_article_date(self, dom) -> datetime:
        pass

    def get_article_writer(self, dom) -> str:
        pass

    def get_article_text(self, dom) -> str:
        pass

    def parse_article(self,dom) -> Article:
        pass
