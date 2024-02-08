import html_ex as ex
from bs4 import BeautifulSoup
soup = BeautifulSoup(ex.html_example, 'html.parser')
print(soup.find('div'))
print(soup.find('div', {'id': 'text_id2'}))
div_text = soup.find('div', {'id': 'text_id2'})
div_text = soup.find('div', id= 'text_id2')
print(div_text.text)
print(div_text.string)

'''
    <div id="text_id2">
        Example page
        <p>g</p>
    </div>
'''

href_link = soup.find('a', {'class': 'internal_link'}) # 딕셔너리 형태
href_link = soup.find('a', class_='internal_link') # class_사용: class는 파이썬 예약어
print(href_link) # <a class="internal_link", ...>
print(href_link['href']) # <a>태그 내부 href 속성의 값(url)을 추출
print(href_link.get('href')) # ['href']와 동일 기능
print(href_link.text) # <a> Page1 </a>태그 내부의 텍스트(Page1) 추출
'''
<a class="internal_link" href="/pages/page1.html">Page1</a>
'''
print('href_link.attrs: ', href_link.attrs) # <a>태그 내부의 모든 속성 출력
print('class 속성값: ', href_link['class']) # class 속성의 value 출력
print('values():', href_link.attrs.values()) # 모든 속성들의 값 출력
values = list(href_link.attrs.values()) # dictionary 값들을 리스트로 변경
print('values[0]: {0}, values[1]: {1}'.format(values[0], values[1]))



#<a class="external_link"  href="www.google.com">google</a>
href_value = soup.find(attrs={'href' : 'www.google.com'})
href_value = soup.find('a', attrs={'href': 'www.google.com'})
print('href_value: ', href_value)
print(href_value['href'])
print(href_value.string)

#<span class="red">BeautifulSoup Library Examples!</span>

span_tag = soup.find('span')
print('span tag:', span_tag)
print('attrs:', span_tag.attrs)
print('value:', span_tag.attrs['class'])
print('text:', span_tag.string)

