import time

import requests

class Fetcher:
    def __init__(self):
        pass

    def fetch(self,url):
        print(url)
        res = None
        try:
            res = requests.get(url)
        except requests.exceptions.MissingSchema:
            print("ungültige url")

        time.sleep(1)
        return res
