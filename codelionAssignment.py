## 스켈레톤 코드

## importing library
import requests
import pandas as pd
from bs4 import BeautifulSoup
import bs4
import json

## 키 값을 가져오고 그 키값을 통해서 크롤링 위치로 이동합니다. parameter = {"directorNm: "}을 통해서 봉준호 감독의 작품만을 얻어옵니다.
 ## 코드 작성 1
## key 작성

key = '97d3bd242902fe1d3ce040690de00cc9'

## url 작성
url = "http://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=" + key


## parameter 작성
parameter = {"directorName": "봉준호"}


## request 작성

save = requests.get(url, parameter)



# request 받아온 내용을 json 파일로 변경해주세요 -> .json 사용
# 그 결과를 html이라는 변수에 담아주세요.
 ## 코드 작성 2
## json형식으로 request 를 받아주세요 변수명은 html로 해주시면 좋을 것 같아요.

html= save.json()

html


DF = pd.DataFrame(html['movieListResult']["movieList"])
## 연도로 다시 정렬
DF = DF.sort_values("prdtYear")

## 컬럼 형식 바꾸기
DF['directors'] = DF['directors'].apply(lambda x : x[0]['peopleNm'])
DF['companys'] = DF['companys'].apply(lambda x : x[0]['companyNm'] if x else x)

DF
