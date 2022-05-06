from bs4 import BeautifulSoup
import requests
from datetime import datetime

url = "http://www.daum.net/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
rank = 1

results = soup.findAll('a','link_favorsch')
search_rank_file = open("rankresult.txt","w")



print(datetime.today().strftime("%Y year %m month %d is the date of the real-time chart.\n"))

for result in results:
    search_rank_file.write(str(rank)+"rank:"+result.get_text() + "\n")
    print(rank,"rank : ",result.get_text(),"\n")
    rank += 1