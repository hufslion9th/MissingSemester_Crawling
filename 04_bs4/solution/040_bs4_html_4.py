# ----------------------------------------------------
# AI교육원의 페이지 링크를 출력하세요.
# ----------------------------------------------------

from bs4 import BeautifulSoup

# 1. url 대신 html 파일을 불러옵니다.

html = open("bs4_html.html", encoding="utf-8")

# 2. Soup 객체를 생성합니다.
soup = BeautifulSoup(html, "html.parser")

# 3. a태그를 불러오고 두번째 링크를 찾습니다.
a = soup.select_one("div#hyperlink a:nth-child(2)")
print(a)

# 4. ai교육원의 링크를 불러옵니다.
link = a.attrs["href"]
print(link)
