# ----------------------------------------------------
# 목록 1, 2, 3을 각각 출력하고 모두 출력해보세요.
# ----------------------------------------------------

from bs4 import BeautifulSoup

# 1. url 대신 html 파일을 불러옵니다.
html = open("bs4_html.html", encoding="utf-8")

# 2. Soup 객체를 생성합니다.
soup = BeautifulSoup(html, "html.parser")

# 3. 목록 1을 출력합니다.

# 4. 목록 1과 2를 출력합니다.

# 5. 목록을 모두 출력합니다.
