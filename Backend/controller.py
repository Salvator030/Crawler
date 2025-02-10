import threading
from threading import Thread

from Backend.Crawler.MainCrawler import MainCrawler
from Backend.Orm.OrmHandler import OrmHandlerFactory
from Backend.Orm.OrmModels import Article

import json

from Backend.controller_threads import CrawlAndPersistArticlesThread

class Controller:

    def __init__(self):
        self.__article_handler = OrmHandlerFactory().create_handler(Article)
        self.__threads: {str, Thread} = {}

    def start_crawler(self) -> str:
        msg = ""
        if not "CrawlAndPersistArticlesThread" in self.__threads.keys():
            thread = CrawlAndPersistArticlesThread()
            thread.name = "CrawlAndPersistArticlesThread"
            thread.start()
            self.__threads["CrawlAndPersistArticlesThread"] = thread
            msg = ""
            if thread.is_alive():
                msg = "Crawler is Started"
            else:
                msg = "Crawler is not Started"
        else:
            msg = "Crawler is running "
        json_objects = {"msg": msg }
        return json.dumps(json_objects, indent=4)

    def stop_crawler(self) -> str:
        msg = "Crawler is not run"
        if "CrawlAndPersistArticlesThread" in self.__threads.keys():
            thread = self.__threads["CrawlAndPersistArticlesThread"]
            msg = "Crawler will be stopped "
            if not thread._stop_event.is_set():
                thread.stop()
                thread.join()
                msg = "Crawler is Stop"
            self.__threads.pop("CrawlAndPersistArticlesThread")
        json_objects = {"msg": msg}
        return json.dumps(json_objects, indent=4)




    def get_all(self) -> str:
        articles = self.__article_handler.get_all_articles()
        json_objects = [article.json() for article in articles]
        return json.dumps(json_objects, indent= 4)
