# ----------------------------------------------------
# 아래 문장을 출력하세요
# “p태그가 위치한 공간입니다. id는 p1입니다.”
# ----------------------------------------------------

from bs4 import BeautifulSoup

# 1. url 대신 html 파일을 불러옵니다.
html = open("bs4_html.html", encoding="utf-8")

# 2. Soup 객체를 생성합니다.
soup = BeautifulSoup(html, "html.parser")

# 3. 텍스트를 추출합니다.
p1 = soup.find("p", id="p1")
print(p1.string)
print(p1.text)
