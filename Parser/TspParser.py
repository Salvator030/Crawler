from bs4 import BeautifulSoup, NavigableString, PageElement
from datetime import datetime

from django.template.defaultfilters import first
from django.utils.lorem_ipsum import paragraphs

from Parser.ParserInterface import ParserInterface
from Orm.OrmModels.Article import Article
from Orm.OrmModels.Content import Content


class TspParser(ParserInterface):


    def __init__(self):
        self.__tsp_url_prefix = "https://www.tagesspiegel.de"
        self.__article_list_tag = "li"
        self.__article_link_tag = "a"

        self.__headline_tag = "span"
        self.__first_headline_tag_data_ob="kicker"
        self.__second_headline_tag_data_ob = "headline"
        self.__third_headline_tag = "p"
        self.__third_headline_tag_html = None

        self.__content_tag = "div"
        self.__content_tag_id="story-elements"
        self.__writer_tag = "span"
        self.__writer_tag_property = "author"
        self.time_tag = "time"

    def parse_requests(self, res):
        return BeautifulSoup(res.text, 'html.parser')

    def get_free_articles_urls(self,res: BeautifulSoup):
        main_content = res.find("main")
        articles = main_content.find_all(self.__article_list_tag)
        free_articles = []
        for e in articles:

            if e.find("svg") is None :
                    href = e.find_next(self.__article_link_tag).attrs["href"]
                    if href.endswith(".html"):
                        url = self.__tsp_url_prefix + href
                        free_articles.append(url)
        return free_articles


    def get_article_header(self,dom: BeautifulSoup):

        spans = dom.find_all(self.__headline_tag)
        first_headline = ""
        second_headline = ""
        description = ""
        for span in spans:
            if "data-ob" in span.attrs:
                if span.attrs["data-ob"] == self.__first_headline_tag_data_ob:
                    first_headline = span.text
                elif span.attrs["data-ob"] == self.__second_headline_tag_data_ob:
                    second_headline = span.text
                    tag = span.find_next(self.__third_headline_tag)
                    description =  tag.text
        header = [first_headline, second_headline,
                  description]
        return header

    def get_article_date(self,dom: BeautifulSoup) -> datetime:

        date_string: str = dom.find("time").attrs["datetime"]
        date =  datetime.fromisoformat(date_string)
        return  date


    def get_article_writer(self,dom: BeautifulSoup):
        writer = dom.find(self.__writer_tag,property=self.__writer_tag_property)
        if writer is not None:
            return writer.contents[0].text
        elif dom.find("em") is not None:
            return dom.find("em").contents[0]
        else:
            return  "unknown"

    def get_article_content( self,dom: BeautifulSoup):

        story_elements =  dom.find(self.__content_tag,id= self.__content_tag_id)

        lines = []
        p_list = story_elements.find_all("p")

        for line in p_list:
            for element in line.contents:

                if len(line.contents) == 1:
                    lines.append(line.contents[0])
                else:
                    for content in line.contents:
                        if content == NavigableString:
                            lines.append(content)
                        else:
                            lines.append(content.text)

        text = ""
        for e in lines:
            text += str(e)

        content = Content(text=text)
        return content

    def parse_article(self,dom):
        date = self.get_article_date(dom)
        header = self.get_article_header(dom)
        content = self.get_article_content(dom)
        content.date = date
        writer = self.get_article_writer(dom)
        publisher = "TSP"

        article =  Article(data=date,headline= header[0], sub_headline = header[1],  description = header[2], writer= writer,publisher= publisher)

        article.contents.append(content)
        return  article