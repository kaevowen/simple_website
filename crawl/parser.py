from bs4 import BeautifulSoup as bs
import os
import requests
import html.parser
import json
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CLIENT_ID = '0ZH4Jxq2Sil2c_0uNWm6'
CLIENT_SECRET = 'PM4PbNyF68'
headers = {"X-Naver-Client-Id": CLIENT_ID, "X-Naver-Client-Secret": CLIENT_SECRET}
url = 'https://openapi.naver.com/v1/search/news.json?display=20&query=' + '우한'


def crawl_naver_news():
    req = html.unescape(requests.get(url, headers=headers).json())
    return req['items']
