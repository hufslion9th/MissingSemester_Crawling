from selenium import webdriver
from bs4 import BeautifulSoup

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

#다나와 아이패드 상품명, 가격 크롤러 만들기
browser = webdriver.Chrome('./webdriver/chromedriver.exe')

# 크롬 내부 대기
browser.implicitly_wait(5)

# 브라우저 사이즈 설정
browser.set_window_size(1920, 1280)

#페이지 이동
browser.get('http://prod.danawa.com/list/?cate=12210596&15main_12_02')

WebDriverWait(browser,5).until(EC.presence_of_element_located( (By.CSS_SELECTOR, '#searchMakerRep1452') ) ).click()
time.sleep(2)



cur_page = 1
max_page = 6
f = open('./result/ipadinfo.txt', 'w', encoding='UTF-8')
#----------------------------------------------------------------------------
while(cur_page <= max_page):
    #bs4 객체를 생성
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    #상품 리스트 prod_list
    prod_list = soup.select('div.main_prodlist.main_prodlist_list > ul > li')
    #print(prod_list)

    for product in prod_list:
        if(product.select_one('div.prod_rel_content')):
            prod_name = product.select_one('p.prod_name > a').text.strip()
            prod_price = product.select_one('p.price_sect > a > strong').text.strip()
            #print(prod_name)
            #print(prod_price)
            text = "상품명: {}, 가격: {}\n".format(prod_name, prod_price)
            f.write(text)

    cur_page += 1 # 2, 
    if(cur_page > max_page):
        break
    WebDriverWait(browser,3).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.number_wrap > a:nth-child({})'.format(cur_page)))).click()
    time.sleep(3)

#파일 닫기
f.close()

#브라우저 닫기
browser.close()