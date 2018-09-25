from bs4 import BeautifulSoup
import urllib2
import csv
from halo import Halo


csvfile = csv.writer(open('reddit.csv', 'w'))

csvfile.writerow(["topic", "url", "votes"])

pages = int(raw_input("enter number of pages to scrap:"))

url = 'https://www.reddit.com/'

i = 1

while pages > 0:

    request = urllib2.Request(url)

    request.add_header(
        'User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0')

    myurlopener = urllib2.build_opener()

    myurl = myurlopener.open(request)

    spinner = Halo(text="Processing Page", spinner="dots")

    spinner.start()

    myurldata = myurl.read()

    soup = BeautifulSoup(myurldata, 'lxml')

    # find the div containing data and iterate over it
    for choice in soup.find_all('div', class_='thing'):

        topicName = choice.find('p', class_='title').a.text.encode(
            'utf-8')             # get the topic name

        topicUrl = choice.find('p', class_='title').a.get(
            'href').encode('utf-8')   # get the url of the topic

        votes = choice.find('div', class_='score unvoted').text.encode(
            'utf-8')     # get the number of votes on topic

        # get the subreddit topic name
        topic = choice.find('a', class_="subreddit hover may-blank").text[2:]

        # if url is not valid then convert it into a valid url
        if choice.find('p', class_='title').a.get('href').startswith('/r/'):

            csvfile.writerow(
                [topicName, 'https://www.reddit.com' + topicUrl, votes, topic])

        else:

            csvfile.writerow([topicName, topicUrl, votes, topic])

    # get the url of the next page to fetch
    url = soup.find('span', class_='next-button').a.get('href')

    spinner.stop()

    pages = pages - 1

    print "\nPage Number " + str(i) + " complete"

    i = i + 1



print "Scraping Complete"
