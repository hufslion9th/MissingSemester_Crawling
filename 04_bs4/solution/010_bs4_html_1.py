# ----------------------------------------------------
# 이 웹 페이지의 페이지 이름을 출력하세요.
# ----------------------------------------------------

from bs4 import BeautifulSoup

# 1. url 대신 html 파일을 불러옵니다.
html = open("bs4_html.html", encoding="utf-8")

# 2. Soup 객체를 생성합니다.
soup = BeautifulSoup(html, "html.parser")

# 3. find와 태그명을 사용해 이동
title = soup.find("title")
print(title)


# 4. 문자열 출력

# string으로 문자열만 추출
print(title.string)

# text로 문자열만 추출
print(title.text)

# 또는 get_text()으로 문자열만 추출
print(title.get_text())

# 완료!
