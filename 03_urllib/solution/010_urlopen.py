# 1. urllib을 불러오세요
# urllib.request는 URL을 가져오기 위한 파이썬 모듈입니다.
import urllib.request

# 2. 가져오고 싶은 주소를 가져옵니다 : 네이버 검색결과
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%ED%95%9C%EA%B5%AD%EC%99%B8%EB%8C%80"

# 3. urllib의 urlopen으로 검색한 결과를 가져옵니다.
search_result = urllib.request.urlopen(url)

# 4. 헤더 확인하기
print(search_result.info())

# 5. 웹 페이지 상태 확인하기 : HTTP 응답코드
print(search_result.status)

# 6. HTML 코드 불러오기 : 정제되지 않은 코드
print(search_result.read())
