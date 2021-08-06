# crawling
import requests
from bs4 import BeautifulSoup

# time sleep
from time import sleep

# data handling
import pandas as pd

# [변수 선언]
search = input("검색어를 입력하세요 : ")
page_number = int(input("검색하고 싶은 최대 페이지 번호를 입력하세요. : "))

title_list = []  # 도서 제목
author_list = []  # 작가
link_list = []  # 구매링크
origin_price_list, sell_price_list = [], []  # 가격정보

# [Query 를 보냅니다.]
# vPstrKeyWord : 검색어
# currentPage : 현재 페이지
for page in range(1, page_number + 1):
    print(f"\t{page} 페이지의 도서 정보를 수집 중 입니다.", end="  ")

    url = "엔드포인트 까지의  주소를 입력하세요"

    # 요청을 보냅니다. 상단 쿼리정보 (vPstrKeyWord...)를 확인하고 적절한 변수를 입력해주세요
    response = requests.get(
        url, params={"vPstrKeyWord": 적절한 변수를 입력해주세요, 
                    "currentPage": 적절한 변수를 입력해주세요
        })

    # soup 객체를 만듭니다.
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.select("#search_list tr")


    for book in books:
        # [css selector를 이용해 도서 제목, 작가, 정가, 판매가를 추출하고, 리스트에 추가하세요.]
        # hint! books에서 tr 까지 불러왔다는 것을 기억하세요

        # 예시 : title
        title = book.select_one("td.detail > div.title > a > strong").string
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

        # [attrs를 사용해 도서 구매 링크를 추출하고, 리스트에 추가하세요]
        link = book.select_one(css selector를 입력하세요).attrs[가져오고 싶은 속성의 key값을 입력합니다.]
        link_list.append(link)


    # 서버의 부하를 줄이기 위해 3초동안 쉽니다
    sleep(3)


# ----------------------------------------------------------------------
# 여기부터는 수정하지 마세요


# [csv 파일에 데이터를 저장합니다.]
df = pd.DataFrame(
    {
        "title": title_list,
        "author": author_list,
        "origin_price": origin_price_list,
        "sell_price": sell_price_list,
        "purchase": link_list,
    })

print("\nCreating DataFrame ...")
df.to_csv("kyobobook_lv1.csv", index=False, encoding="utf-8")

print("수집한 데이터를 csv 파일로 저장 중입니다.")
result = pd.read_csv("kyobobook_lv2.csv")


# 저장된 csv 파일 확인
sample = 3
print("\n\033[33mComplete!\033[0m")
print(f"저장이 완료되었습니다. 상위 {sample}개 항목을 출력합니다.")
print("-----" * 30)
print(result.head(sample))
print("-----" * 30)
print(f"\n저장된 데이터는 총 {result.shape[0]}행 {result.shape[1]}열 입니다.\n")
