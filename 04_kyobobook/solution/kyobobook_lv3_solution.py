# crawling
import requests
from bs4 import BeautifulSoup

# data handling
import pandas as pd

# time sleep
from time import sleep
import random
import os


# [Query 를 보냅니다.]
# vPstrKeyWord : 검색어
# currentPage : 현재 페이지
# row : 페이지 당 목록 개수
def search_pages(search, page_number, row_number):
    print("\nCollecting ...")
    print(f"{search}의 검색 결과 중 \033[33m도서제목, 작가, 가격 및 구매링크\033[0m를 수집합니다.")

    for page in range(1, page_number + 1):
        print(f"\t{page} 페이지의 {row_number} 번째 항목까지 수집 중 입니다.", end="  ")

        # 엔드포인트 까지의  주소를 "url" 변수에 담아주세요.
        url = "https://search.kyobobook.co.kr/web/search?"

        # 상단의 쿼리를 이용해 get 방식으로 요청을 보내고, 그 결과를 "response" 변수에 담아주세요.
        response = requests.get(
            url, params={"vPstrKeyWord": search, "currentPage": page, "row": row_number}
        )

        # "soup" 변수에 response를 이용해 soup 객체를 생성합니다.
        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.select("#search_list tr")

        # collect 함수 실행 코드 : 수정 X
        books = soup.select("#search_list tr")
        collect(books)


def collect(books):
    for book in books:
        # [css selector를 이용해 도서 제목, 작가, 정가, 판매가를 추출하고, 리스트에 추가하세요.]
        # hint 1! books에서 tr 까지 불러왔다는 것을 기억하세요
        # hint 2! select가 아닌 select_one을 사용해야 합니다.

        # 예시 : title
        title = book.select_one("td.detail > div.title > a > strong").string
        title_list.append(title)

        # your code here : author
        author = book.select_one("td.detail > div.author > a").string
        author_list.append(author)

        # your code here : origin_price
        origin_price = book.select_one("td.price > div.org_price > del").string
        origin_price_list.append(origin_price)

        # your code here : sell_price
        sell_price = book.select_one("td.price > div.sell_price > strong").string
        sell_price_list.append(sell_price)

        # [attrs를 사용해 도서 구매 링크를 추출하고, 리스트에 추가하세요]
        link = book.select_one("td.detail > div.title > a").attrs["href"]
        link_list.append(link)

    # sleep을 이용해 2초에서 4초 사이의 시간을 무작위하게 쉬는 코드를 작성하세요
    pause = random.uniform(2, 4)
    print(f"(sleep : {int(pause)}sec)")
    sleep(pause)


# ----------------------------------------------------------------------
# 여기부터는 데이터 저장 코드입니다. 수정하지 마세요


# [csv 파일에 데이터를 저장합니다.]
def create_df(filename):
    df = pd.DataFrame(
        {
            "title": title_list,
            "author": author_list,
            "origin_price": origin_price_list,
            "sell_price": sell_price_list,
            "purchase": link_list,
        }
    )

    print("\nCreating DataFrame ...")
    df.to_csv(f"{filename}.csv", index=False, encoding="utf-8")

    print(f"수집한 데이터를 csv 파일로 저장 중입니다.")
    result = pd.read_csv(f"{filename}.csv")
    return result


# 저장된 csv 파일 확인
def check_data(sample, result):
    os.system("cls")
    print("\n\033[33mComplete!\033[0m")
    print(f"저장이 완료되었습니다. 상위 {sample}개 항목을 출력합니다.")
    print("-----" * 30)
    print(result.head(sample))
    print("-----" * 30)
    print(f"\n저장된 데이터는 총 {result.shape[0]}행 {result.shape[1]}열 입니다.\n")


# ----------------------------------------------------------------------


def main():
    # [변수 선언]
    # "search 변수에" 검색어를 입력받습니다. (type : str)
    search = input("검색어를 입력하세요 : ")

    # "page_number" 변수에 검색하고 싶은 페이지 번호를 입력받습니다. (type : int)
    page_number = int(input("검색하고 싶은 최대 페이지 번호를 입력하세요. : "))

    # "row_number" 변수에 한 페이지에 확인하고 싶은 도서의 개수를 입력받습니다.. (type : int)
    row_number = int(input("한 페이지에 확인하고 싶은 도서의 개수를 입력하세요. : "))

    # [수집]
    global title_list, author_list, link_list, origin_price_list, sell_price_list
    title_list = []  # 도서 제목
    author_list = []  # 작가
    link_list = []  # 구매링크
    origin_price_list, sell_price_list = [], []  # 가격정보
    search_pages(search, page_number, row_number)

    # [데이터 저장] : create_df(원하는 파일 이름, 원하는 파일 형태)
    result = create_df("kyobobook_lv3")

    # [저장된 데이터 확인]
    check_data(3, result)


if __name__ == "__main__":
    main()
