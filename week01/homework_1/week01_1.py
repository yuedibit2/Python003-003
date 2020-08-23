# 使用requests库获取猫眼电影名称、电影类型、上映时间

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

def visit_url(myurl):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'

    #referer='https://maoyan.com'

    header = {'user-agent':user_agent}

    response = requests.get(myurl,headers=header)

    bs_info=bs(response.text,'html.parser')

    return bs_info

myurl = 'https://maoyan.com/films?showType=3'
bs_info=visit_url(myurl)

movie_name=[]
plan_time=[]
movie_categorys=[]

# 获取电影名称和上映时间
for tags in bs_info.find_all('div', attrs={'class': 'movie-item film-channel'},limit=10):
    ntag=tags.find('span',attrs={'class':'name'})
    movie_name.append(ntag.text)  # 电影名称
    atag=tags.find_all('div',attrs={'class':'movie-hover-title'})
    movie_categorys.append(list(atag[1].stripped_strings)[1])  #电影类型
    plan_time.append(list(atag[3].stripped_strings)[1])  #上映时间

print(movie_name)
print(movie_categorys)
print(plan_time)

my_movie={'电影名称':movie_name,'电影类型':movie_categorys,'上映时间':plan_time}
df_movie=pd.DataFrame(my_movie,columns=['电影名称','电影类型','上映时间'])
df_movie.to_csv('./maoyan_movie.csv',encoding='gbk',index=False)
