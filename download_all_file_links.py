# To download all links in a webpage

##################################################################################################
# IMPORTs
from bs4 import BeautifulSoup
import requests
import time
import urllib3
import os
import re

# website to crawl
url = "https://web.archive.org/web/20170712033340/http://www.princeton.edu/~verdu/mud/solutions/"

r = requests.get(url)  #
data = r.text
soup = BeautifulSoup(data)

rgx_pattern = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
prefix = "https://web.archive.org"

for link in soup.find_all("a"):
    #http = urllib3.PoolManager()
    #response = http.request("GET", link.get("href"))
    #time.sleep(8)
    #soup = BeautifulSoup(response.data.decode("utf-8"))
    print(link.get("href"))
    x = requests.get(link.get("href"))
    time.sleep(10)
    d = x.text
    s = BeautifulSoup(d)
    #print(s)
    for l in s.find_all("a"):
        print(l)
        y = str(l.get("href"))
        print(y)
        z = prefix + y
        print(z)
        q = requests.get(z)
        w = q.content
        with open(z, "wb") as f:
            f.write(w)
