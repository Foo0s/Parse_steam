import requests
from bs4 import BeautifulSoup
import fake_useragent

class Parse_cs_TM:
    def __init__(self, url_req) -> None:
        self.URL = f"https://market.csgo.com/ru/?search={url_req}"
        self.fake_us = fake_useragent.UserAgent(browsers=["yandex", 'chrome', "firefox"])
        self.HEADERS = {"Accept": "application/json, text/plain, */*",
                        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
                        "Cookie": "cf_clearance=KWiGg_9DqiJoFaxZrmqjjgYU8Hstm.xiqfRlkNjkBnA-1681066230-0-160; PHPSESSID=63195507de7d19e74b63bcf1dff2e376; _ga_TEWB4TCDHF=GS1.1.1681066237.1.1.1681066525.0.0.0; _ga=GA1.1.1965270832.1681066237; _ga=GA1.3.1965270832.1681066237; _gid=GA1.3.61995176.1681066238; _ym_uid=1681066238581618168; _ym_d=1681066238; _ym_isad=2; _ym_visorc=b",
                        "User-Agent": self.fake_us.random
                        }
        

    def search_info(self):
        response = requests.get(self.URL, headers=self.HEADERS)
        soup = BeautifulSoup(response.text, "lxml")
        a = open("sasd.html", "w")
        b = a.write(str(soup))



a = Parse_cs_TM("Пустынный повстанец")
print(a.search_info())