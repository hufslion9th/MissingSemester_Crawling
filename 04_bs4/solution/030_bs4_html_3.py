# ----------------------------------------------------
# 목록 1, 2, 3을 각각 출력하고 모두 출력해보세요.
# ----------------------------------------------------

from bs4 import BeautifulSoup

# 1. url 대신 html 파일을 불러옵니다.
html = open("bs4_html.html", encoding="utf-8")

# 2. Soup 객체를 생성합니다.
soup = BeautifulSoup(html, "html.parser")

# 3. 목록 1을 출력합니다.
li_1 = soup.select("div#selector > ul > li:nth-child(1)")
print(li_1)

# 4. 목록 1과 2를 출력합니다.
li_12 = soup.select("div#selector > ul > li:nth-child(-n+2)")
print(li_12)

# 5. 목록을 모두 출력합니다.
li_all = soup.select("div#selector > ul > li")
print(li_all)
