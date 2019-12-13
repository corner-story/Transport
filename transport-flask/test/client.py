from config import URL
import requests

class Client(object):
    def __init__(self, URL=URL, headers={'Content-Type': 'application/json; charset=utf-8'}):
        self.URL = URL
        self.headers = headers
        self.session = requests.Session()

    def get(self, api, params=None):
        if params == None:
            return self.session.get(self.URL+api, headers=self.headers)
        return self.session.get(self.URL+api, params=params, headers=self.headers)
    
    def post(self, api, data=None):
        if data == None:
            return self.session.post(self.URL+api, headers=self.headers)
        return self.session.post(self.URL+api, json=data, headers=self.headers)
