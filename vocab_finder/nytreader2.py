# from bs4 import BeautifulSoup
# from bs4.element import Comment
# import urllib.request
#
# def tag_visible(element):
#     if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
#         return False
#     if isinstance(element, Comment):
#         return False
#     return True
#
# def text_from_html(body):
#     soup = BeautifulSoup(body, 'html.parser')
#     texts = soup.findAll(text = True)
#     visible_texts = filter(tag_visible, texts)
#     return u" ".join(t.strip() for t in visible_texts)
#
# html = urllib.request.urlopen("https://www.nytimes.com/2009/12/21/us/21storm.html")
# print(text_from_html(html))

import os, ssl
if(not os.environ.get('PYTHONHTTPVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context
import nltk
dler = nltk.downloader.Downloader()
dler._update_index()
nltk.download('punkt')
dler._status_cache['panlex_lite'] = 'installed'
from newspaper import Article

url = 'https://www.nytimes.com/2009/12/21/us/21storm.html'
nyt_article = Article(url, language = 'en')
nyt_article.download()
nyt_article.parse()
nyt_article.nlp()
print(nyt_article.text)
