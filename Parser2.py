

import pickle
import requests
import json
import ast

#open list of 'known' words.

with open('wordlist.txt', 'rb') as fp:
    b = pickle.load(fp)

# scrape Article

import os, ssl
if(not os.environ.get('PYTHONHTTPVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context
import nltk
dler = nltk.downloader.Downloader()
dler._update_index()
nltk.download('punkt')
dler._status_cache['panlex_lite'] = 'installed'
from newspaper import Article

url = 'https://www.newyorker.com/news/our-columnists/why-measles-is-a-quintessential-political-issue-of-our-time?utm_campaign=aud-dev&utm_source=nl&utm_brand=tny&utm_mailing=TNY_Daily_030319&utm_medium=email&bxid=5be9db7a3f92a40469e970ed&user_id=53272341&esrc=&utm_term=TNY_Daily'
nyt_article = Article(url, language = 'en')
nyt_article.download()
nyt_article.parse()
nyt_article.nlp()

# Put the article's words into a list


artlist = nyt_article.text.split()

hist =[]
for i in artlist:
    if i not in hist:
        hist.append(i)

# for i in hist:
#     if i not in b:
#         try:
#             app_id = '86931dcd'
#             app_key = '4046b9d828fef4483ea27f076bb59391'
#
#             language = 'en'
#             word_id = i
#
#             url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()
#
#             r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
#             definition = r.text
#
#
#             print(ast.literal_eval(definition)['results'][0]['id'] + ': ' + ast.literal_eval(definition)['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0] + '\n\n')
#         except:
#             pass
            #print(i + ' not found.\n\n')

print(artlist[:10])
print(b[:10])
print(hist[:10])
