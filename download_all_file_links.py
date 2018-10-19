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
test = "https://web.archive.org/web/20060919125641/http://www.princeton.edu/~verdu/mud/solutions/7/7.1.huaidai.ps"

#'''

r = requests.get(url)  # main site = page with Table of Contents
data = r.text
soup = BeautifulSoup(data)

for link in soup.find_all("a"):  # for each problem
    #print(link.get("href"))  # link = each problem
    r = requests.get(link.get("href"), allow_redirects=True)
    d = r.text
    s = BeautifulSoup(d)

    for sol_link in s.find_all("a"):  # for each solution file to each problem
        try:
            #print(sol_link)
            link_string = str(sol_link.get("href"))
            print("Problem link: " + link_string)
            url_parts = link_string.split("solutions/")
            k = url_parts[1].split("/")  # get just problem number and name of soln author
            #print("J: " + str(j))
            #print("K: " + str(k))
            full_problem_url = prefix + link_string
            #print("Full url for problem: " + full_problem_url)
            q = requests.get(full_problem_url)
            w = q.url
            print("Url of full problem url: " + w)
            r = requests.get(w, stream=True)
            if not os.path.exists("solutions"):
                os.makedirs("solutions")

            file_path = os.path.join(os.getcwd(), "solutions")
            file = os.path.join(file_path, k[1])
            print("File: " + file)
            with open(file, "wb") as f:
                f.write(r.content)

        except IndexError:
            continue

        except ConnectionError:
            continue
'''

####
# test 1 download
r = requests.get(test, stream=True)
print(r.status_code)
print(os.getcwd())
g = "test.ps"
file = os.path.join(os.getcwd(), g)


print(file)
with open(file, "wb") as f:
    f.write(r.content)

'''
