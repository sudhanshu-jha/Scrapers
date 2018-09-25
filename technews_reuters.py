from bs4 import BeautifulSoup

import requests

import csv


source = requests.get('https://www.reuters.com/news/archive/technologyNews?view=page').text

soup = BeautifulSoup(source, 'lxml')


csv_file = open('reuter_output.csv', 'w')


csv_writer = csv.writer(csv_file)

csv_writer.writerow(['Headline', 'Summary', 'Article Link'])


for article in soup.find_all('article'):

    headline = article.find('h3', class_='story-title').text

    print(headline)

    summary = article.find('div', class_='story-content').p.text

    print(summary)

    try:

        article_src = article.find('a', href=True)

        article_link = 'https://www.reuters.com/{}'.format(article_src['href'])

    except Exception as e:

        article_link = None

    print(article_link)

    print()

    csv_writer.writerow([headline, summary, article_link])


csv_file.close()
