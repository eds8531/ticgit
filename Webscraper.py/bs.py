import requests, bs4
res = requests.get('https://www.nytimes.com/2019/03/01/opinion/john-dean-michael-cohen.html?action=click&module=Opinion&pgtype=Homepage')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
print(noStarchSoup)
