import pymysql
from selenium import webdriver
from bs4 import BeautifulSoup as BeautifulSoup

conn = pymysql.connect(
    host='localhost', 
    user="root",
    database= "mydatabase",
    password= "**********",
    charset='utf8')

url = 'https://www.melon.com/chart/index.htm'
driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source
bs4 = BeautifulSoup(html, 'html.parser')
song_parts = bs4.select('tbody > tr')

sql = "INSERT INTO melon_top_100 (title, singer, album, likes) VALUES (%s, %s, %s, %s)"

with conn:
    with conn.cursor() as cur:
        for song in (song_parts):
            title = song.find('div', class_= 'ellipsis rank01').get_text().replace('\n', '')
            singer = song.find('span', class_= 'checkEllipsis').get_text().replace('\n', '')
            album = song.find('div', class_= 'ellipsis rank03').get_text().replace('\n', '').replace("'", "\'")
            likes = song.find('button', class_ = 'button_etc like').get_text().replace('\n', '').replace('좋아요총건수', '').replace(',', '')
            cur.execute(sql, (title, singer, album, likes))
            conn.commit()

driver.quit()
