import html_ex as ex # 변수 갖고오기 : ex.html_example
from bs4 import BeautifulSoup
soup = BeautifulSoup(ex.html_example, 'html.parser')
# print(soup.title) # <title> 태그 전체를 가져옴
# print(soup.title.string) # <title>태그의 텍스트만 리턴
# print(soup.title.get_text()) # .string, .text(예전 버전)와 동일한 기능
#print(soup.title.parent) # 해당 태그를 포함하는 부모


#print(soup.body) # body에 접근

# print(soup.h1)
# print(soup.h1.string)

print(soup.a)
print(soup.a.string) # <a> 태그 내부의 텍스트 추출 (google)
print(soup.a['href']) # <a> 태그 내부의 href 속성의 url을 추출
print(soup.a.get('href')) # a['href']와 동일 기능