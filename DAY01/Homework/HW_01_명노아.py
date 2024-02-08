from bs4 import BeautifulSoup
from urllib.request import urlopen

url="https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.Yst5ji9yxTY"

def scraping_use_find(html) :
    bs=BeautifulSoup(html,"html.parser")
    bs2=bs.find("main", class_="container")
    bs3=bs2.find("div", class_="contentArea")
    bs4=bs3.find("div", id="seven-day-forecast")
    bs5=bs4.find("div", class_="panel-body")
    bs6=bs5.find("div", id="seven-day-forecast-container")
    bs7=bs6.find("ul", id="seven-day-forecast-list")
    bs8=bs7.find_all("li", class_="forecast-tombstone")
    print('''
National Weather Service Scraping
----------------------------------
[find 함수 사용]''')
    print(f"총 tomestone-container 검색 개수 : {len(bs8)}")
    for i in range(0,10) :
        print("----------------------------------------------------------------------------------")
        if i==9 :
            break
        sample=bs8[i].find("div", class_ = "tombstone-container")
        print(f'[Peroid] : {sample.find("p", class_="period-name").text}')
        try :
            print(f'[Short desc] : {sample.find("p", class_="short-desc").text}')
        except AttributeError:
            print(f'[Short desc] : No Information')
        try : 
            print(f'[Temperature] : {sample.find("p", class_="temp").text}')
        except AttributeError:
            print(f'[Temperature] : No Information')
        print(f'[Image desc] : {sample.find("img", class_="forecast-icon").get("title")}')
        
def scraping_use_select(html) :
    br=BeautifulSoup(html,"html.parser")
    br2=br.select_one("main.container > div.contentArea")
    br3=br2.select_one("div#seven-day-forecast > div#seven-day-forecast-body > div#seven-day-forecast-container > ul#seven-day-forecast-list")
    br4=br3.select("li.forecast-tombstone")
    print('''
National Weather Service Scraping
----------------------------------
[select 함수 사용]''')
    print(f"총 tomestone-container 검색 개수 : {len(br4)}")
    for i in range(0,10) :
        print("----------------------------------------------------------------------------------")
        if i==9 :
            break
        sample=br4[i].select_one("div.tombstone-container")
        print(f'[Peroid] : {sample.select_one("p.period-name").text}')
        try :
            print(f'[Short desc] : {sample.select_one("p.short-desc").text}')
        except AttributeError:
            print(f'[Short desc] : No Information')
        try : 
            print(f'[Temperature] : {sample.select_one("p.temp").text}')
        except AttributeError:
            print(f'[Temperature] : No Information')
        print(f'[Image desc] : {sample.select_one("img.forecast-icon").get("title")}')

scraping_use_find(urlopen(url))
scraping_use_select(urlopen(url))