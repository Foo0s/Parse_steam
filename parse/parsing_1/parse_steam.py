import requests
from bs4 import BeautifulSoup
import googletrans
import re
import fake_useragent

class Parse:
    def __init__(self, url):
        self.url_name = url
        self.url = f"https://steamcommunity.com/market/search?appid=730&q={url}#p1_price_asc"
        self.ua = fake_useragent.UserAgent(browsers=['chrome', 'edge', 'firefox', 'yandex'])
        self.HEADERS = {"Accept": "*/*",
                        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
                        "User-Agent": self.ua.random}

    def get_req(self):
        self.response = requests.get(self.url, headers=self.HEADERS)
        self.soup = BeautifulSoup(self.response.text, "lxml")

    def get_data(self, flag=1):
        result = []
        if flag == 1:
            try:
                item_name = self.soup.find("div", id="result_0")
                price = item_name.find("span", class_="normal_price").get_text()
                price_text = re.findall(r"\d+.\d\d", str(price))
                quantity = item_name.find("span", class_="market_listing_num_listings_qty").get_text()
                img = item_name.find("img", id="result_0_image")
                result.append({"Название предмета": item_name["data-hash-name"], "Цена": f"От ${price_text[-1]} до ${price_text[0]}", "Количество": quantity, "Изображение": img["src"]})
                return result
            except Exception:
                return "Предмет не найден"
        else:
            k = 0
            all_items = self.soup.find_all("a", class_="market_listing_row_link")
            for i in all_items:
                price_items = i.find("div", class_='market_listing_price_listings_block').get_text().split("\n")
                sort_price = re.findall(r"\d+.\d\d", str(price_items))
                result.append({"Название предмета": i.find("div", "market_listing_item_name_block").get_text().split("\n")[1],
                            "Цена": f"От ${sort_price[-1]} до ${sort_price[0]}",
                            "Количество": int(i.find("div", class_="market_listing_right_cell market_listing_num_listings").get_text().replace("\n", "")),
                            "image": i.find("img", class_='market_listing_item_img')['src']})
                k += 1
            return result



