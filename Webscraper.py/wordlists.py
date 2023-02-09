import requests
import pickle

url = 'https://www.gutenberg.org/files/15659/15659-h/15659-h.htm'
r = requests.get(url)

html = r.text

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
#type(soup)

text = soup.get_text()

import re

wlist = re.findall('\w+', text)

histw = []
hist =[]
wordlist = []
for i in wlist:
    if i.lower() in histw:
        for j in hist:
            if i.lower() == j[0]:
                j[1] += 1
    else:
        histw.append(i.lower())
        hist.append([i.lower(), 1])

def sortSecond(val):
    return val[1]
hist.sort(key = sortSecond, reverse = True)
for i in hist:
    print(i)

for i in hist:
    if i[1] >= 5:
        wordlist.append(i[0])

with open('wordlist.txt', 'wb') as fp:
    pickle.dump(wordlist, fp)
