from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs,'\n') # 타이틀 이름을 출력
print(bs.h1,'\n') # 웹사이트에서 첫 번째 <h1> 태그만 반환
print(bs.h1.string,'\n') # .string: 태그 내부의 문자열만 가져옴


print(bs.title)
print('title:', bs.title.string)