from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
#정규식
import re
import time

# https://instagram.com/robots.txt
# robots.txt -> 크롤링 규약
# disallow / allow

# so chromedriver is assuming that chrome has crashed
chrome_options = webdriver.ChromeOptions()
# 밑의 옵션은 크롬을 안보고 진행하는 것
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-suage')
# 안전하지 않음 오류 제거
chrome_options.add_argument('ignore-certificate-errors')

# /c/program/python
# ./file : 현재경로
# ../file : 한칸 위로 올라감
# 설치되어있는 크롬 실행
driver = webdriver.Chrome("./chromedriver", options=chrome_options)

#인스타 접속
driver.get('https://www.instagram.com')
#접속로딩을 고려한 타임슬립 시간 설정
# 시간을 넉넉히 설정합니다.
# 유저가 들어갔을때 => 아이디 넣는 시간 비밀번호 넣는 시간.
time.sleep(5)

# 로그인에 필요한 사항을 브라우저 제어를통해 입력합니다.
email = 'your email' # 사용할 계정 정보 입력
# 로그인 창 선택
# loginForm > div > div:nth-child(1) > div > label >input'
input_id = driver.find_elements_by_css_selector(
   '#loginForm > div > div:nth-child(1) > div > label >input')[0]
# print(input_id)
# 혹시나 로그인창에 뭐가 적혀있을 수 도 있어서 아이디창 비우기
input_id.clear()
# id창에 email 넣어줌
input_id.send_keys(email)


password = 'your password' #비번 정보 수정
input_pw = driver.find_elements_by_css_selector(
    '#loginForm > div > div:nth-child(2) > div > label >input')[0]
input_pw.clear()
input_pw.send_keys(password)

# id와pw제출
input_pw.submit()
# 로그인 끝

time.sleep(3)
word = "고양이" # 검색할 해시태그, 띄어쓰기 사용하면 안됨
# 태그검색 url
# https://www.instagram.com/explore/tags/%EA%B3%A0%EC%96%91%EC%9D%B4/
# url encode 를 원하거나 한글로 보고싶은 경우에는
# https://meyerweb.com/eric/tools/dencoder/ 들어가서 encode/decode 하면됨

url = 'https://www.instagram.com/explore/tags/' + word
driver.get(url)
time.sleep(2)

#한 줄로 찾아봄
#row = driver.find_elements_by_css_selector("div.Nnq7c.weEfm")
#print(row)
#for r in row:
#    r.click()

# 첫게시물을 여는 함수를 정의합니다
def select_first(driver):
    first = driver.find_element_by_css_selector("div._9AhH0")
    first.click()
    time.sleep(5)

 # 내용을 가져오는 함수를 정의합니다.
def get_content(driver):
    html = driver.page_source
    # lxml이 기본적으로 bs4에서 제공해주는 것보다 속도가 빠름
    # pip install lxml
    soup = BeautifulSoup(html, 'lxml') # 내가 원하는데로 안가져오는 경우
    try:
        content = soup.select('div.C4VMK > span')[0].text
    except:
    # 에러가날경우에는 빈칸을 준다.
        content = ' '
    # 정규표현식을 활용하여 해시태그를 가져옵니다.
    tags = re.findall(r'#[^\s#,\]+', content)
    # 작성일자를 가져옵니다.
    date = soup.select('time._1o9PC.Nzb55')[0]['datetime'][:10]
    # 좋아요 수를 가져옵니다.
    try:
        like = soup.select('div.Nm9Fw.zV_Nj > span')[0].text.replace(',', '')
    except:
        like = 0
    # 위치정보를 가져옵니다.
    try:
        place = soup.select('div.M30cS')[0].text
    except:
        place = ''
    # 수집한 정보를 리스트로 저장합니다.
    row = []
    # row.append(content)
    # row.append(date)
    data = [content, date, like, place, tags]
    return data

# 다음게시글을 여는 함수를 정의합니다.
def move_next(driver):
    right = driver.find_element_by_css_selector(
    'a.coreSpriteRightPaginationArrow')
    right.click()
    time.sleep(5)
# 함수를 차례대로 실행합니다.
# (5)개 게시물 보기
select_first(driver)
result = []
max_post = 5
for i in range(5):
    try:
        data = get_content(driver) 
        result.append(data)
        move_next(driver)
    except:
        time.sleep(2)
        move_next(driver)
#print(result[:1])

# 데이터프레임 만들고 엑셀로 저장하기
results_df = pd.DataFrame(result)
results_df.columns = ['content', 'data', 'like', 'place', 'tags']
results_df.to_excel('crawling_sample.xlsx', index=False)
