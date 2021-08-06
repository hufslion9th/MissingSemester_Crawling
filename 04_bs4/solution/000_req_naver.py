# 네이버 검색 프로그램 만들기

import requests

# 1. 페이지 정보를 가져옵니다.
url = "https://search.naver.com/search.naver"

# 2. 검색어를 입력합니다.
search = input("검색하고 싶은 검색어를 입력하세요 : ")
response = requests.get(url, params={"query": search})

# 3. 통신이 성공했는지 확인합니다.
print(response)

# 4. html 정보를 불러옵니다.
print(response.text)
