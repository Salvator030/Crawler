from datetime import datetime

from bs4 import BeautifulSoup, NavigableString

from Backend.Orm.OrmModels import Article, Content
from Backend.Crawler.Parser.ParserInterface import ParserInterface




class SpiegelParser(ParserInterface):

    def __init__(self):

        self.__article_list_tag = "article"
        self.__article_link_tag = "a"
        self.__svg_tag_id = "spon-spon-paid-flag-m"

        self.__first_headline_tag = "h2"
        self.__second_headline_tag_class = "RichText RichText--sans leading-loose lg:text-xl md:text-xl sm:text-l lg:w-10/12 md:w-10/12 lg:mx-auto md:mx-auto lg:px-24 md:px-24 sm:px-16 lg:mb-32 md:mb-32 sm:mb-24 text-center z-20"

        self.__date_tag = "time"
        self.__writer_tag_class = "text-black dark:text-shade-lightest font-bold border-b border-shade-light hover:border-black dark:hover:border-white"
        self.__content_section_class = "lg:mt-32 md:mt-32 sm:mt-24 md:pb-48 lg:pb-48 sm:pb-32"
        self.__content_tag = "p"
    def parse_requests(self, res):
        return BeautifulSoup(res.text, 'html.parser')


    def get_free_articles_urls(self, res):
        try:
            # get all article
            articles: BeautifulSoup = res.find_all(self.__article_list_tag)
            free_articles = []

            # check if the artice have a audio,video,pay-wal, gallery icon. when then continue
            for e in articles:
               if e.find_next("svg",id=self.__svg_tag_id) is not None:
                   continue
               elif e.find_next("svg",id="spon-video-flag-m") is not None:
                    continue
               elif e.find_next("svg", id="spon-11f-flag-m")is not None:
                   continue
               elif e.find_next("svg", id="spon-gallery-flag-m")is not None:
                   continue
               elif e.find_next("svg", id="spon-audio-flag-m")is not None:
                   continue

               # when not append the href attribut to list with free article
               else:
                  href = e.find_next(self.__article_link_tag).attrs["href"]
                  free_articles.append(href)
            return free_articles
        except* Exception as e:
            print(f"SpiegelParser.get_free_articles_urls() ERROR")
            print(e.exceptions)

    def get_article_header(self, dom: BeautifulSoup):
        try:
            description = dom.find(self.__first_headline_tag).find_next_sibling()
            if description is not None:
                description = description.text.strip()
            else:
                description = ""
            header = [dom.find(self.__first_headline_tag).find_next().text.strip(),
                      dom.find(self.__first_headline_tag).text.split("\n")[-2],
                      description]
            return header
        except * Exception as e:
            print(f"SpiegelParser.get_article_header() ERROR")
            print(e.exceptions)
            

    def get_article_date(self, dom: BeautifulSoup) -> datetime:
        try:
            date_string = dom.find(self.__date_tag)
            if date_string is not None:
                date = datetime.fromisoformat(date_string.attrs["datetime"])
                return date
            return datetime.now()
        except* Exception as e:
            print(f"SpiegelParser.get_article_date() ERROR")
            print(e.exceptions)

    def get_article_writer(self, dom):
        try:
            writer = dom.find("a", class_=self.__writer_tag_class)
            if writer is not None:
                return writer.text
            else:
                return "unknown"
        except* Exception as e:
            print(f"SpiegelParser.get_article_writer() ERROR")
            print(e.exceptions)

    def get_article_content(self, dom) -> Content:
        try:
            content_section = dom.find(class_=self.__content_section_class)
            p_list = content_section.find_all(self.__content_tag)
            lines = []
            for p in p_list:
                if len(p.contents) == 1:
                   lines.append(p.contents[0])
                else:
                   for content in p.contents:
                       if content == NavigableString:
                           lines.append(content)
                       else:
                           lines.append(content.text)
            text = ""
            for e in lines:
                text += str(e)
            return Content(text=text)
        except* Exception as e:
            print(f"SpiegelParser.get_article_content() ERROR")
            print(e.exceptions)



    def parse_article(self, dom):

            date = self.get_article_date(dom)
            header = self.get_article_header(dom)
            content = self.get_article_content(dom)
            content.date = date
            writer = self.get_article_writer(dom)
            publisher = "SPIEGEL"

            if header is not None and  content.text != "":
                article = Article(data=date, headline=header[0], sub_headline=header[1], description=header[2], writer=writer,
                                  publisher=publisher)
                article.contents.append(content)
                return article
            else:
                return None



