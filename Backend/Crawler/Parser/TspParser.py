from bs4 import BeautifulSoup, NavigableString
from datetime import datetime

from Backend.Crawler.Parser.ParserInterface import ParserInterface
from Backend.Orm.OrmModels.Article import Article
from Backend.Orm.OrmModels.Content import Content


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
        try:
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
        except* Exception as e:
            print(f"TspParser.get_free_articles_urls() ERROR")
            print(e.exceptions)

    def get_article_header(self,dom: BeautifulSoup):
        try:
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
        except* Exception as e:
            print(f"TspParser.get_article_header() ERROR")
            print(e.exceptions)

    def get_article_date(self,dom: BeautifulSoup) -> datetime:
        try:
            date_string: str = dom.find("time").attrs["datetime"]
            date =  datetime.fromisoformat(date_string)
            return  date
        except* Exception as e:
            print(f"TspParser.get_article_date() ERROR")
            print(e.exceptions)


    def get_article_writer(self,dom: BeautifulSoup):
        try:
            # TODO the function does not work correctly.
            # if no author is specified, the description of the article is sometimes entered
            output = ""
            writer = dom.find(self.__writer_tag,property=self.__writer_tag_property)
            if writer is not None:
                output = writer.text
                print(f"1: {output}")
            elif dom.find("em") is not None:
                output = dom.find("em").text
                print(f"2: {output}")
            else:
                output =  "unknown"
                print(f"3: {output}")
            # Workaround... because TODO
            if len(output) > 50:
                output = "PARSE ERROR"
            return output
        except* Exception as e:
            print(f"TspParser.get_article_writer() ERROR")
            print(e.exceptions)


    def get_article_content( self,dom: BeautifulSoup):
        try:
            story_elements =  dom.find(self.__content_tag,id= self.__content_tag_id)

            lines = []
            p_list = story_elements.find_all("p")

            for line in p_list:


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
            print(text)
            content = Content(text=text)
            return content
        except* Exception as e:
            print(f"TspParser.get_article_content() ERROR")
            print(e.exceptions)

    def parse_article(self,dom):

        article = None
        try:
            date = self.get_article_date(dom)
            header = self.get_article_header(dom)
            content = self.get_article_content(dom)
            content.date = date
            writer = self.get_article_writer(dom)
            publisher = "TSP"

            temp_article =  Article(data=date,headline= header[0], sub_headline = header[1],  description = header[2], writer= writer,publisher= publisher)
            temp_article.contents.append(content)
            article = temp_article
            print(f"Parsed article: {article}")
        except*Exception as e:
            print(f"TspParser.parse_article() ERROR")
            print(e.exceptions)
        finally:
            return  article