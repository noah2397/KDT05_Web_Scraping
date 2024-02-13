# § colspan=2로 설정된 부분 처리
# • html_table_parser 라이브러리 사용
# – make2d() 함수: 2차원 리스트 형태로 변환
# • Pandas의 DataFrame으로 변환 후 csv 파일로 저장
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parse # 설치한 모듈을 갖고옴
import pandas as pd
html = urlopen('http://en.wikipedia.org/wiki/Comparison_of_text_editors')
bs = BeautifulSoup(html, 'html.parser')
# 두 개의 테이블 중에 첫 번째 테이블 사용: find_all() 사용
#table = bs.find_all('table', {'class':'wikitable'})[0]
table = bs.find('table', {'class':'wikitable'}) # 테이블을 찾은 다음에,
table_data = parse.make2d(table) # 2차원 리스트 형태로 변환
# 테이블의 2행을 출력
print('[0]:', table_data[0])
print('[1]:', table_data[1])

# Pandas DataFrame으로 저장 (2행부터 데이터 저장, 1행은 column 이름으로 사용)
df = pd.DataFrame(table_data[2:], columns=table_data[1])
print(df.head())
# csv 파일로 저장
csvFile = open('editors1.csv', 'w', encoding='utf-8') # t: text mode
writer = csv.writer(csvFile)
for row in table_data[1:]:
    writer.writerow(row)
csvFile.close()