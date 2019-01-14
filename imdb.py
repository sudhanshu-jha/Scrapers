from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin  # For joining next page url with base url

search_terms = input("What movie do you want to know about?\n> ").split()

url = "http://www.imdb.com/find?ref_=nv_sr_fn&q=" + "+".join(search_terms) + "&s=all"


def scrape_find_next_page(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    next_page = soup.find("td", "result_text").find("a").get("href")

    return next_page


next_page_url = scrape_find_next_page(url)

new_page = urljoin(url, next_page_url)


def scrape_movie_data(next_page_url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(next_page_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    title_year = soup.find("span", "titleYear").find("a").get_text()

    return title_year


print(scrape_movie_data(new_page))
