# ----------------------------------------------------
# 아래 문장들을 출력하세요
# “p태그가 위치한 공간입니다. id는 p1입니다.”
# “p태그가 위치한 공간입니다. id는 없습니다.”
# ----------------------------------------------------

from bs4 import BeautifulSoup

# url 대신 html 파일을 불러옵니다.
html = open("bs4_html.html", encoding="utf-8")

# Soup 객체를 생성합니다.
soup = BeautifulSoup(html, "html.parser")

# 3. 여러 태그를 추출하는 작업입니다.
p = soup.find_all("p")
print(p)

# + 문자열만 추출하면 어떻게 될까요?
# print(p.string)   # 에러 발생

# string은 한 태그만 불러올 수 있습니다.

# 4. 여러 태그를 불러온 결과에서 문자열만 추출하고 싶다면 for문을 사용하세요.
for line in p:
    print(line.string)
