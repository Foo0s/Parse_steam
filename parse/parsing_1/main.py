import requests
from bs4 import BeautifulSoup
import googletrans

class Parse:
    def __init__(self, url):
        self.url = f"https://steamcommunity.com/market/search?appid=730&q={self.translate(url)}#p1_price_asc"
        self.HEADERS = {"Accept": "*/*",
                        "Cookie": "recentlyVisitedAppHubs=221410; timezoneOffset=10800,0; _ga=GA1.2.2097589957.1678819639; browserid=2869395941980293502; strInventoryLastContext=730_2; steamLoginSecure=76561198325682559%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MEQxRl8yMjQ3RjYyMl83QTE4OSIsICJzdWIiOiAiNzY1NjExOTgzMjU2ODI1NTkiLCAiYXVkIjogWyAid2ViIiBdLCAiZXhwIjogMTY4MDc3MDUzOSwgIm5iZiI6IDE2NzIwNDMwOTAsICJpYXQiOiAxNjgwNjgzMDkwLCAianRpIjogIjBEMUFfMjI1NjREODFfMTUxOTUiLCAib2F0IjogMTY3OTc0Nzg1NSwgInJ0X2V4cCI6IDE2OTc2ODIxMzMsICJwZXIiOiAwLCAiaXBfc3ViamVjdCI6ICIzNy4xNDUuMTY3LjIwMSIsICJpcF9jb25maXJtZXIiOiAiOTUuMTUzLjE2My4yMzYiIH0.ge-1919mtFCx8wiSYEU0eUAlsI4yeYxhjiqVljhT5vpcxDKRYuoLSn0bZ2cWJKdT_-tD5ybVXrPbZBrF9KoXCg; _gid=GA1.2.506386064.1680683092; sessionid=c5f9fbbe1196dd6bbb2d5a3d; webTradeEligibility=%7B%22allowed%22%3A1%2C%22allowed_at_time%22%3A0%2C%22steamguard_required_days%22%3A15%2C%22new_device_cooldown_days%22%3A0%2C%22time_checked%22%3A1680768453%7D",
                        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0"}

    def translate(self, word):
        self.trans = googletrans.Translator()
        self.translate = self.trans.translate(text=word, dest='en').text

    def get_req(self):
        self.response = requests.get(self.url, headers=self.HEADERS)
        self.soup = BeautifulSoup(self.response.text, "lxml")

    def get_data(self):
        item_name = self.soup.find("div", id="result_0")["data-hash-name"]
        return item_name


if __name__ == "__main__":
    dt = Parse("glitter")
    dt.get_req()
    info = dt.get_data()
    print(info)
