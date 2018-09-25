import requests
from bs4 import BeautifulSoup
import threading

def crawl(num) :
	
	url="https://www.linkedin.com/directory/companies-a-"+str(num)+"/"
	name = url.split("/")
	name = name[4]
	fname = name+":failure_log"
	fw1 = open(name, "a")
	fw2 = open(fname, "a")
	urls=[url]
	company_url = []
	failed_url = []
	while len(urls) > 0:
		sc = requests.get(urls[0])
		pt = sc.text
		soup = BeautifulSoup(pt,"lxml")
		print len(urls)
		
		try:
			i = soup.find('ul',{'class':'column dual-column'})
			for tag in i.find_all('li'):
				l = tag.find("a").get("href")
				l = str(filter(lambda x:ord(x) > 31 and ord(x) < 128, l))
				if "company" in l:
					company_url.append(l)
					continue
				urls.append(l)
		except:
			failed_url.append(urls[0])
			pass

		urls.pop(0)

	for i in company_url:
		fw1.write(i+"\n")
	fw1.write("\nCOMPLETED")
	for i in failed_url:
		fw2.write(i+"\n")
	fw2.write("\nCOMPLETED")
		
T=threading.Thread		
for j in range(1,101) :
	while threading.active_count()>5:
		continue
	t=T(target=crawl,args=(j,))
t.start()