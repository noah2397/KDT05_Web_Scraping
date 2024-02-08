from urllib.parse import quote
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = f"https://search.naver.com/search.naver?query={quote('대구+날씨')}"
html = urlopen(url)

# 이후에 BeautifulSoup 등을 사용하여 HTML 파싱을 진행할 수 있습니다.

bs=BeautifulSoup(html, 'html.parser')
print(f'현재 위치 : {bs.find("div",class_="title_area").find("h2").text}')
print(f'현재 온도 : {bs.find("div",{"class":"temperature_text"}).find("strong").text[5:]}')
print(f'날씨 상태 : {bs.find("span",{"class":"weather before_slash"}).text}')
dataList = bs.find("ul",{"class":"today_chart_list"}).find_all("li",{"class":"item_today"})
print("공기 상태 : ")
for i in range(len(dataList)) :
    print(f'{dataList[i].find("a").find("strong").text} {dataList[i].find("a").find("span").text}')
print('''
-----------------------
시간대별 날씨 및 온도
-----------------------''')
dataList = bs.find("div",{"class":"graph_inner _hourly_weather"}).find("ul").find_all("li",class_="_li")
for i in range(len(dataList)) :
    time = dataList[i].find("dl").find("dt").text
    status = dataList[i].find("dl").find("dd", class_="weather_box").find("i").text
    ondo = dataList[i].find("dl").find("dd", class_="degree_point").select_one("div > div > span").text
    print(f"{time}  {status}  {ondo}")











