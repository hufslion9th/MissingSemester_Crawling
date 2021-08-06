# 1. urllib을 불러오세요
# urllib.request는 URL을 가져오기 위한 파이썬 모듈입니다.
import urllib.request

# 2. 가져오고 싶은 이미지의 주소를 복사합니다.
# e.g. 한국외대 글로벌캠퍼스 40주년 로고
img_url = "https://www.hufs.ac.kr/user/hufs/mycodyimages/sub01/01_010601j_01.jpg"

# 3. img_url에 담긴 이미지 정보입니다.
img = urllib.request.urlopen(img_url).read()

# 4. with open(파일 경로, 모드) as 파일 객체:
with open("hufsglobal_40_urlopen.png", "wb") as f:
    f.write(img)
