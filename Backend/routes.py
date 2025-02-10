from flask import Flask
from . import app
from .controller import Controller

controller = Controller()

@app.route("/")
def is_server_run():
    return "Data-Crawler-Server is run"

@app.route("/get_all")
def get_all():
    return controller.get_all()

@app.route("/start_crawler")
def start_crawler():
    return controller.start_crawler()

@app.route("/stop_crawler")
def stop_crawler():
    return controller.stop_crawler()

