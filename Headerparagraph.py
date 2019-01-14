from urllib2 import urlopen
from urllib2 import HTTPError
from bs4 import BeautifulSoup


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        title = bsObj.body.h1
        title = bsObj.body.p
    except AttributeError as e:
        return None
    return title


title = getTitle("http://www.pythonscraping.com")
if title is None:
    print("Title could not be found")
else:
    print(title)
