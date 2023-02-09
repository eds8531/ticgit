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

artlist = nyt_article.text.split()
histw = []
hist =[]
for i in artlist:
    if i in histw:
        for j in hist:
            if i == j[0]:
                j[1] += 1
    else:
        histw.append(i)
        hist.append([i, 1])

def sortSecond(val):
    return val[1]
hist.sort(key = sortSecond, reverse = True)
for i in hist:
    print(i)
