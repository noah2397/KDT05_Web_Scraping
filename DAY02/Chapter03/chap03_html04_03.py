#chap03_html04_03.py

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')
# next_siblings 속성
for sibling in soup.find('table', {'id': 'giftList'}).tr.next_siblings:
    print(sibling)