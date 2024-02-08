# 예외 처리
# • 페이지를 찾을 수 없는 경우
# – 404 Page Not Found 에러 발생: HTTPError 예외 발생 시킴
# • 서버를 찾을 수 없는 경우
# – 500 Internal Server Error 발생시 URLError 예외 발생 시킴



from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
try:
    html = urlopen('http://www.pythonscraping.com/pages/error.html')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found!')
else:
    print('It worked!')