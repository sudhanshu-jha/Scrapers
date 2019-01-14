import requests
from bs4 import BeautifulSoup

url = "https://www.babynamesdirect.com/"

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
g_data1 = soup.find_all("a", {"class": "boy"})
g_data2 = soup.find_all("a", {"class": "girl"})
boys = []
girls = []

for item in g_data1:
    boys.append(item.text)

for item in g_data2:
    girls.append(item.text)

f = open("names.csv", "w")

for key in boys:
    f.write(key + "," + "boy")
    f.write("\n")

for key in girls:
    f.write(key + "," + "girl")
    f.write("\n")

f.close()
