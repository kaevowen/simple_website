from django.shortcuts import render
from bs4 import BeautifulSoup as bs
import requests


def wuhan_crawl(req):
    client_id = '0ZH4Jxq2Sil2c_0uNWm6'
    client_secret = 'PM4PbNyF68'
    url = 'https://openapi.naver.com/v1/search/news.xml?query=' + '우한'
    headers = {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret" : client_secret}
    req = bs(requests.get(url, headers=headers).content, 'lxml')

    lst = []
    for r in req.find_all('title'):
        lst.append(r.text)

    return render(req, 'crawl/crawl_result.html', lst)

# Create your views here.
