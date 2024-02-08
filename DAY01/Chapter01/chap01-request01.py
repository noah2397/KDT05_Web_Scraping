from urllib.request import urlopen
from bs4 import BeautifulSoup

# 샘플 코드 1
# urllib.error.HTTPError: HTTP Error 406: Not Acceptable 발생
melon_url = 'https://www.melon.com/chart/index.htm'
html = urlopen(melon_url)
soup = BeautifulSoup(html.read(), 'html.parser')
print(soup)