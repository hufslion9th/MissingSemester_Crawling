# ----------------------------------------------------------------
# 난이도를 위해 일부 기능을 축소했습니다.
# 실시간 실습의 완성본을 원하시면 lv2를 완성해주세요.
# ----------------------------------------------------------------

# crawling
import requests
from bs4 import BeautifulSoup

# time sleep
from time import sleep

# [변수 선언]
search = input("검색어를 입력하세요 : ")
page_number = int(input("검색하고 싶은 페이지 번호를 입력하세요. : "))

title_list = []  # 도서 제목
author_list = []  # 작가
link_list = []  # 구매링크
origin_price_list, sell_price_list = [], []  # 가격정보

# [Query 를 보냅니다.]
# vPstrKeyWord : 검색어
# currentPage : 현재 페이지
url = "https://search.kyobobook.co.kr/web/search?"  # 엔드포인트 까지의  주소

# 요청을 보냅니다. 
response = requests.get(url, params={"vPstrKeyWord": search, "currentPage": page_number})
                
# soup 객체를 만듭니다.
books = BeautifulSoup(response.text, "html.parser")


for book in books:
    # [css selector를 이용해 도서 제목, 작가, 정가, 판매가를 추출하고, 리스트에 추가하세요.]

    # 예시 : title
    title = book.select_one("#search_list > tr:nth-child(10) > td.detail > div.title > a > strong").string
    title_list.append(title)

    # your code here : author
    author = book.select_one(css selector를 입력하세요).string
    author_list.append(author)

    # your code here : origin_price
    origin_price = book.select_one(css selector를 입력하세요).string
    origin_price_list.append(origin_price)

    # your code here : sell_price
    sell_price = book.select_one(css selector를 입력하세요).string
    sell_price_list.append(sell_price)

    # [attrs(attributes)를 사용해 도서 구매 링크를 추출하고, 리스트에 추가하세요]
    link = book.select_one(css selector를 입력하세요).attrs["href"]
    link_list.append(link)

    # 서버의 부하를 줄이기 위해 3초동안 쉽니다
    sleep(3)


# 출력코드
print('수집한 책의 제목')
print(title_list)

print('수집한 책의 저자 정보')
print(author_list)

print('수집한 책의 정가')
print(origin_price_list)

print('수집한 책의 판매가')
print(sell_price)

print('수집한 책의 구매 링크')
print('link_list')