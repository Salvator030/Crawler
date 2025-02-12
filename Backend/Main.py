from Backend.Crawler import MainCrawler
from Backend.Controller.controller_threads import CrawlAndPersistArticlesThread


def thread_function( stop_event):
   crawler = MainCrawler()
   while not stop_event.is_set():
      crawler.crawl_all_news_papers()

class Main:
   # fetcher =Fetcher()
   # url = "https://www.tagesspiegel.de/internationales/wir-sind-auf-alle-szenarien-vorbereitet-baltische-staaten-wollen-sich-am-samstag-von-russlands-stromnetz-abkoppeln-13162444.html"
   # s_url = "https://www.spiegel.de/partnerschaft/haushalt-und-arbeitsteilung-maenner-ueberschaetzen-ihren-beitrag-zur-hausarbeit-a-97078671-2a83-46a7-aa52-e5b576664e50"

   # parser = TspParser()
   #
   # factory = OrmHandlerFactory()
   # article_handler: ArticleHandler = factory.create_handler(Article)
   # crawler_factory = CrawlerFactory()
   # tsp_crawler= crawler_factory.create_crawler(TspCrawler)
   # spiegel_crawler = crawler_factory.create_crawler(SpiegelCrawler)
   # a = spiegel_crawler.crawl_article(s_url)

   # print(tsp_crawler.crawl_article(url))



   # while True:
   #    articles: [Article] = spiegel_crawler.crawl_articles()
   #    [print(a) for a in articles]
   #    article_handler.add_articles(articles)
   #    articles = tsp_crawler.crawl_articles()
   #    print(articles)
   #    article_handler.add_articles(articles)
   # [print(i) for i in article_handler.get_all_articles()]


   # crawler.start()
   # d = fetcher.fetch(url)
   # dom = parser.parse_requests(d)
   # p = parser.get_x_posts(dom)
   # a = parser.parse_article(dom)
   # a.x_posts = interactor.search_for_x_posts(url)
   # [print(e) for e in l]
   # print(a)
   # db = Database(DatabaseOption())
   # en = db.connect()
   # db.insert_Models(en,[a])
   # interactor.search_for_x_posts("https://www.tagesspiegel.de/internationales/bei-besuch-in-damaskus-syriens-machthaber-verweigert-baerbock-den-handschlag-12959740.html")

   t = CrawlAndPersistArticlesThread()
   t.name = "crawl"
   ts = [t]

   [print(e.name) for e in ts ]


   # stop_event = threading.Event()
   # thread = threading.Thread(target=thread_function, args=(stop_event,))
   # thread.start()
   # i =""
   #
   # while i != "ja":
   #    i = input("abbrechen")
   # stop_event.set()
   # thread.join()
   # print("ende")



