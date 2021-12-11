import requests
# from bs4 import BeautifulSoup
# from collections import Mapping

URL = 'https://auto.ria.com/car/hyundai/'
HEADERS = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.1.932 Yowser/2.5 Safari/537.36',
           'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r



def parse():

    html = get_html(URL)
    print(html)



parse()