import requests
from bs4 import BeautifulSoup

class CityBoroughCrawler:
    @staticmethod
    def get_city_list():
        target = 'https://www.kobis.or.kr/kobis/business/mast/thea/findTheaterSchedule.do'
        response = requests.get(target)
        soup = BeautifulSoup(response.text, 'html.parser')
        cities = soup.find("div", {"class": "schedule"}).find("ul").find_all("li")
        for city in cities:
            yield ({
                "city_seq": city["wideareacd"],
                "city_name": city.text.strip(),
            })

    @staticmethod
    def get_borough_list(city_seq: str):
        target = 'https://www.kobis.or.kr/kobis/business/mast/thea/findBasareaCdList.do'
        response = requests.post(target, data={
            'sWideareaCd': city_seq
        })
        
        for data in response.json()["basareaCdList"]:
            yield {
                "borough_seq": data["cd"],
                "borough_name": data["cdNm"],
                "city_seq": city_seq
            }
            