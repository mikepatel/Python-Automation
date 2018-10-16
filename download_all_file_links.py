# To download all links in a webpage

##################################################################################################
# IMPORTs
from bs4 import BeautifulSoup
import requests
import os

# website to crawl
url = "https://web.archive.org/web/20170712033340/http://www.princeton.edu/~verdu/mud/solutions/"

rgx_pattern = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"

prefix = "https://web.archive.org"

# url to test
test = "https://web.archive.org/web/20060917084044/http://www.princeton.edu/~verdu/mud/solutions/1/1.3.xinwang.ps"

#'''

r = requests.get(url)  #
data = r.text
soup = BeautifulSoup(data)

for link in soup.find_all("a"):
    print(link.get("href"))
    x = requests.get(link.get("href"), allow_redirects=True)
    d = x.text
    s = BeautifulSoup(d)

    for l in s.find_all("a"):
        try:
            print(l)
            y = str(l.get("href"))
            print("Y: " + y)
            j = y.split("solutions/")
            k = j[1].split("/")
            print("J: " + str(j))
            print("K: " + str(k))
            z = prefix + y
            print("Z: " + z)
            q = requests.get(z)
            w = q.url
            print("W: " + w)
            r = requests.get(w, stream=True)
            file = os.path.join(os.getcwd(), k[1])
            print("File: " + file)
            with open(file, "wb") as f:
                f.write(r.content)

        except IndexError:
            continue
'''

####
# test 1 download
r = requests.get(test, stream=True)
print(os.getcwd())
g = "1/1.3.xinwang.ps"
g.replace("/", "\\")
file = os.path.join(os.getcwd(), g)


print(file)
with open(file, "wb") as f:
    f.write(r.content)
'''
