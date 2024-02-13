from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('http://www.pythonscraping.com/pages/warandpeace.html')
driver.implicitly_wait(5)
# find_element(By.CLASS_NAME, '클래스이름'): 하나의 클래스 이름 검색
name = driver.find_element(By.CLASS_NAME, "green") # 1개만 찾는다
print(name.text)
print('-' * 20)
# find_elements(By.CLASS_NAME, '클래스이름'): 해당 클래스 이름을 모두 검색
nameList = driver.find_elements(By.CLASS_NAME, "green")
for name in nameList:
    print(name.text)
driver.quit()