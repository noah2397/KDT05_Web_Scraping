# 오늘 배운 걸 안쓴 버전

from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen("https://finance.naver.com/sise/sise_market_sum.naver")
soup=BeautifulSoup(html,"html.parser")
bs=soup.select_one("#contentarea > div.box_type_l > table.type_2 > tbody")
bs2=bs.select("tr")

info=[]
for i in range(1,14) :
    if i in [6,7,8] :
        continue
    info.append([bs2[i].select("a")[0].text, bs2[i].select("a")[1].get("href").replace('board','main')])


while True :
    print("="*50)
    print("[ 네이버 코스피 상위 10대 기업 목록 ]")
    print("="*50)
    for i,v in enumerate(info) :
        print(f"[{i+1:>2}] {v[0]}")
    value = int(input("주가를 검색할 기업의 번호를 입력하세요(-1: 종료):"))
    if value==-1 :
        break
    url=f"https://finance.naver.com{info[value-1][1]}"
    print(url)
    html=urlopen(url)
    soup=BeautifulSoup(html,"html.parser")
    print("종목명 : " + soup.select_one("#middle > div.h_company > div.wrap_company > h2 > a").text) # 사명
    print("종목코드 : "+soup.select_one("#middle > div.h_company > div.wrap_company > div > span.code").text)
    print("현재가 : "+soup.select_one("div > p.no_today > em > .blind").text) # 현재주가
    data = soup.select("#chart_area > div.rate_info > table > tr")
    data2 = data[0].select("span.blind")
    data3 = data[1].select("span.blind")
    print("전일가 : " + data2[0].text)# 전일
    print("시가 : "+data3[0].text)# 시가
    print("고가 : " +data2[1].text)# 고가
    print("저가 : "+data3[1].text)# 저가