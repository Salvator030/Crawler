import threading
from threading import Thread

from Backend import socketio
from Backend.Orm.OrmHandler import OrmHandlerFactory
from Backend.Orm.OrmModels import Article

from flask_socketio import SocketIO, emit

import json

from Backend.Controller.controller_threads import CrawlAndPersistArticlesThread

class Controller:

    def __init__(self):
        self.__article_handler = OrmHandlerFactory().create_handler(Article)
        self.__threads: {str, Thread} = {}

    def start_crawler(self) -> str:
        msg = 0
        if not "CrawlAndPersistArticlesThread" in self.__threads.keys():
            thread = CrawlAndPersistArticlesThread()
            thread.name = "CrawlAndPersistArticlesThread"
            thread.start()
            self.__threads["CrawlAndPersistArticlesThread"] = thread
            if thread.is_alive():
                msg = 1
            else:
                msg = -1
        else:
            msg = 2
        json_objects = {"msg": msg }
        return json.dumps(json_objects, indent=4)

    import threading
    import json

    def stop_crawler(self) -> str:
        msg = 0
        if "CrawlAndPersistArticlesThread" in self.__threads.keys():
            thread = self.__threads["CrawlAndPersistArticlesThread"]
            if not thread.is_alive():
                msg = -1
            else:
                stop_thread = threading.Thread(target=self._stop_thread, args=(thread,))
                stop_thread.start()
                msg = 1
                self.__threads.pop("CrawlAndPersistArticlesThread")
        json_objects = {"msg": msg}
        return json.dumps(json_objects, indent=4)

    def _stop_thread(self, thread):
        thread.stop()
        thread.join()
        print("Sending 'crawler_stopped' event")  # Füge einen Debug-Print hinzu
        socketio.emit('crawler_stopped', {'msg': 1})

    def all_articles(self) -> str:
        articles = self.__article_handler.get_all_articles()
        json_objects = {"msg": [article.json() for article in articles] }
        return json.dumps(json_objects, indent= 4)

    def crawler_status(self) -> str:
        msg = 0
        if "CrawlAndPersistArticlesThread" in self.__threads.keys():
            msg = 1
        json_objects = {"msg": msg}
        return json.dumps(json_objects, indent=4)

    def articles_by(self,json_data) -> str:

        result = self.__article_handler.get_article_by(json_data)
        json_obj = {"msg": 0}
        print(result)
        if len(result)> 0 :
            json_obj = {"msg": [article.json() for article in result]}
        return json.dumps(json_obj, indent=4)
