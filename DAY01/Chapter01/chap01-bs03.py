# chap01-bs03.py
# 존재하지 않는 태그 접근
# • None 객체 반환
# • None 객체에 접근: AttributeError 발생
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTitle(url, tag):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        #특정 url에서 body 태그 내부에 파라미터로 전달된 tag(‘h2’ 태그)를 검색함
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        value = bsObj.body.find(tag)
    except AttributeError as e:
        return None
    return value
tag='h2'
value = getTitle('http://www.pythonscraping.com/pages/page1.html', tag) 
if value == None:
    print(f'{tag} could not be found')
else:
    print(value)