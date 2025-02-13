from . import app
from Backend.Controller.Controller import Controller

controller = Controller()

@app.route("/")
def is_server_run():
    return "Data-Crawler-Server is run"

@app.route("/start_crawler")
def start_crawler():
    return controller.start_crawler()

@app.route("/stop_crawler")
def stop_crawler():
    return controller.stop_crawler()

@app.route("/crawler_status")
def crawler_status():
    return controller.crawler_status()

@app.route("/all_articles")
def all_articles():
    return controller.all_articles()