#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup as soup



HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36", 'Accept-Language': 'en-US, en;q=0.5'}

page = requests.get("https://orlando.craigslist.org/d/ethernet-cable/search/", headers=HEADERS)
print(page.status_code)



bsobj = soup(page.content,'html.parser')
# bsobj



links = []
for link in bsobj.findAll('li',{'class':'result-row'}):
    links.append(link.a['href'])

# links



title = []

# for link in links:
#     page = requests.get(link, headers=HEADERS)
#     bsobj = soup(page.content,'html.parser')
#     print(bsobj.findAll('h1')[0].text.strip())
#     title.append(bsobj.findAll('h1')[0].text.strip())

#     for i in bsobj.findAll('section',{'id':'postingbody'}):
#         print(i.text.strip())



# len(title)

