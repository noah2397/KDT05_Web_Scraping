from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.naver.com') # 자동으로 네이버에 가서, 2총 있다가 웹 브라우저를 종료한다
print(driver.current_url)
sleep(2)
driver.close()# 하나의 탭만 종료
driver.quit() # webdriver 전체 종료