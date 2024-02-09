import requests
from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
import re
import pandas as pd

data=[]
for page in range(1,52):
    url=f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}&sido=&gugun=&store="
    html=urlopen(url)
    soup=BeautifulSoup(html,"html.parser")
    
    storeInfo = soup.find("tbody").find_all("tr")
    for i,info in enumerate(storeInfo, start=1) :
        filtered_list = list(filter(lambda item: item != "", info.text.split("\n")[2:-1]))
        data.append(filtered_list[0:2]+filtered_list[3:5])
        
        

storeDF=pd.DataFrame(data, columns=["위치(시,구)","매장이름","주소","전화번호"])
order=['매장이름','위치(시,구)','주소','전화번호']
storeDF=storeDF[order]
for i in range(storeDF.shape[0]):
    print(f"[{i:>3}]: ", end="")
    print(f"매장이름 : {list(storeDF.loc[i])[0]},", end=" ")
    print(f"지역 : {list(storeDF.loc[i])[1],}", end=" ")
    print(f"주소 : {list(storeDF.loc[i])[2],}", end=" ")
    print(f"전화번호 : {list(storeDF.loc[i])[3]}")
result=storeDF.to_csv("hollys_branches.csv", encoding='utf-8', index=False)
if result==None : print("hollys_branches.csv 파일 저장 완료")