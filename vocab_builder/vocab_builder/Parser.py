

import ast
import json
from newspaper import Article
import pickle
import re
import requests
import string



# scrape Article

import os, ssl
if(not os.environ.get('PYTHONHTTPVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context
import nltk
dler = nltk.downloader.Downloader()
dler._update_index()
nltk.download('punkt')
dler._status_cache['panlex_lite'] = 'installed'



#Downloads the article to be parsed.

url = 'https://www.nytimes.com/2019/11/18/world/asia/hong-kong-protests.html?action=click&module=Top%20Stories&pgtype=Homepage'
nyt_article = Article(url, language = 'en')
nyt_article.download()
nyt_article.parse()
nyt_article.nlp()

# Opens the known word list.

with open('/Users/ericschlosser/Desktop/TheHardWay/vocab_builder/docs/master_word_list.pickle', 'rb') as f:
    words = pickle.load(f)

f.close()

with open('/Users/ericschlosser/Desktop/TheHardWay/vocab_builder/word_grabber/masterTSL_word_list.pickle', 'rb') as f:
    words1 = pickle.load(f)

f.close()

words = words + words1

# Function for eliminating numbers

def hasNumbers(word):
    return bool(re.search(r'\d', word))

# Puts the article's words into a list


artlist = nyt_article.text.split()

artlist = set(artlist)

artlist = list(artlist)

hist =[]


for i in artlist:
    i = i.translate(str.maketrans('','',string.punctuation))

for i in artlist:
    if i[0] == i[0].upper():
        artlist.remove(i)

for i in artlist:
    i = i.upper()
    if i not in hist:
        if i not in words:
#            if hasNumbers(i) == False:
            if i.isalpha():
                hist.append(i)

# Eliminates words the reader is likely to know.



word_defs = []

for i in hist:
    if i not in word_defs and i not in words:
        word_defs.append(i)

for i in word_defs:
    try:
        print(i)
        app_id = '86931dcd'
        app_key = 'ed68a9f46caa69102ef0e3a720aeb191'

        language = 'en-us'
        word_id = i

        url = 'https://od-api.oxforddictionaries.com/api/v2/entries/' + language + '/' + word_id.lower()

        r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
        definition = r.text

        print('code{}\n'.format(r.status_code))

        print('text\n' + r.text)

        print(ast.literal_eval(definition)['results'][0]['id'] + ': ' + ast.literal_eval(definition)['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0] + '\n\n')
    except:
        pass
