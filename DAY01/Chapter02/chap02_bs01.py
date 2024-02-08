from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://www.daangn.com/hot_articles')  # 당근마켓 URL
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1) # 해당 URL에서 첫 번째 h1 태그를 반환
print(bs.h1.string.strip()) # <h1> 태그 내부의 텍스트만 반환
