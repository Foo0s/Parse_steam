import requests
from bs4 import BeautifulSoup
import googletrans
import re
import fake_useragent

class Parse:
    def __init__(self, url):
        self.url = f"https://steamcommunity.com/market/search?appid=730&q={url}#p1_price_asc"
        self.ua = fake_useragent.UserAgent(browsers=['chrome', 'edge', 'firefox'])
        self.HEADERS = {"Accept": "*/*",
                        "Cookie": "recentlyVisitedAppHubs=221410; timezoneOffset=10800,0; _ga=GA1.2.2097589957.1678819639; browserid=2869395941980293502; strInventoryLastContext=730_2; steamLoginSecure=76561198325682559%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MEQxRl8yMjQ3RjYyMl83QTE4OSIsICJzdWIiOiAiNzY1NjExOTgzMjU2ODI1NTkiLCAiYXVkIjogWyAid2ViIiBdLCAiZXhwIjogMTY4MDc3MDUzOSwgIm5iZiI6IDE2NzIwNDMwOTAsICJpYXQiOiAxNjgwNjgzMDkwLCAianRpIjogIjBEMUFfMjI1NjREODFfMTUxOTUiLCAib2F0IjogMTY3OTc0Nzg1NSwgInJ0X2V4cCI6IDE2OTc2ODIxMzMsICJwZXIiOiAwLCAiaXBfc3ViamVjdCI6ICIzNy4xNDUuMTY3LjIwMSIsICJpcF9jb25maXJtZXIiOiAiOTUuMTUzLjE2My4yMzYiIH0.ge-1919mtFCx8wiSYEU0eUAlsI4yeYxhjiqVljhT5vpcxDKRYuoLSn0bZ2cWJKdT_-tD5ybVXrPbZBrF9KoXCg; _gid=GA1.2.506386064.1680683092; sessionid=c5f9fbbe1196dd6bbb2d5a3d; webTradeEligibility=%7B%22allowed%22%3A1%2C%22allowed_at_time%22%3A0%2C%22steamguard_required_days%22%3A15%2C%22new_device_cooldown_days%22%3A0%2C%22time_checked%22%3A1680768453%7D",
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
                result[0] = {"Название предмета": item_name["data-hash-name"], "Цена": f"От ${price_text[-1]} до ${price_text[0]}", "Количество": quantity, "Изображение": img["src"]}
                return result
            except Exception:
                return "Предмет не найден"
        else:
            k = 0
            all_items = self.soup.find_all("a", class_="market_listing_row_link")
            for i in all_items:
                price_items = i.find("div", class_='market_listing_price_listings_block').get_text().split("\n")
                sort_price = re.findall(r"\d+.\d\d", str(price_items))
                self.item_dop_info = i['href']
                result.append({"Название предмета": i.find("div", "market_listing_item_name_block").get_text().split("\n")[1],
                            "Цена": f"От ${sort_price[-1]} до ${sort_price[0]}",
                            "Количество": int(i.find("div", class_="market_listing_right_cell market_listing_num_listings").get_text().replace("\n", "")),
                            "image": i.find("img", class_='market_listing_item_img')['src']})
                self.search_dop_info(self.item_dop_info, k, result)
                k += 1
            return result
    
    def search_dop_info(self, item, numb, res):
        req = requests.get(item, headers=self.HEADERS)
        soupe = BeautifulSoup(req.text, "lxml")

        req_sell_item = soupe.find("div", class_="responsive_page_frame with_header")
        req_sell = re.findall(r"Запросов на покупку:\W+\d+", req_sell_item.text)
        res[numb]['Запросов на покупку'] = req_sell


a = Parse("Дух воды")
b = a.get_req()
print(a.get_data(2))


