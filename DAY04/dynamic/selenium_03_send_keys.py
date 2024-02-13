# § 텍스트 입력/엔터
# • <input>태그와 같이 입력이 가능한 element는 send_keys()함수로 키 입력이 가능
# • send_keys(‘텍스트’),
# • send_keys(Keys.ENTER)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# ChromeOptions 설정
options = webdriver.ChromeOptions()
# WebDriver 초기화
user_agent_string = 'Mozilla/5.0'
options.add_argument('user-agent=' + user_agent_string)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# WebDriver 초기화
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


# User Agent 정보 추가

driver.get('https://nid.naver.com/nidlogin.login')
driver.implicitly_wait(5)
# <input>의 이름이 id를 검색
driver.find_element(By.NAME, 'id').send_keys('아이디')
driver.find_element(By.NAME, 'pw').send_keys('패스워드') # "아이디"라는 글자와 "패스워드"라는 글자를 입력 후,
#//*[@id="log.login"]
#driver.find_element(By.XPATH,'//*[@id="log.login"]').click() # xpath로도 찾을 수 있다
driver.find_element(By.ID, 'log.login').click() # 로그인 버튼 클릭
driver.quit() # 종료