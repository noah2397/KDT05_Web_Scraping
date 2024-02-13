import pymysql
conn = pymysql.connect(host='localhost',
user='root', passwd='1234', db='scraping', charset='utf8')
cur = conn.cursor()
cur.execute('use scraping')
cur.execute("SELECT * FROM pages WHERE id=2")
print(cur.fetchone())
cur.close()
conn.close()