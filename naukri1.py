import requests
from bs4 import BeautifulSoup
from math import *

url_2 = []
urls_2 = []
f = open("level_1.txt","r")
h = open("log_2.txt","w")
x = f.readlines()
for y in x:
	z = y.strip('\n')
	url_2.append(z)
# print url_2

for url in url_2:
	once_flag = 1
	page_no = 1
	cnt = 1
	name = url
	name = name.split("/")
	name = name[-1]+".txt"
	g = open(name,"w")
	# print url
	try:
		while(page_no<=cnt):
			url_new = url+"-"+str(page_no)
			print url_new
			source_2 = requests.get(url_new)
			text_2 = source_2.text
			# print text_2[:25000]
			soup_2 = BeautifulSoup(text_2)
			if(once_flag==1):
				cnt = soup_2.find('span',{'class':'cnt'}).text.split(" ")
				cnt = ceil(float(cnt[2])/50)
			# print soup_2
			# print "\n", cnt
			i_2 = soup_2.find('div',{'class':'srp_container fl  '})
			# print i_2
			for j_2 in i_2.find_all("div",{'class':'row  '}):
				# print j_2
				k_2 = j_2.find("a").get("href")
				g.write(k_2)
				g.write("\n")
				# urls_2.append(k_2)
				# print k_2
			page_no=page_no+1
			once_flag = 0
	except:
		h.write(url)
		page_no=page_no+1

# print len(urls_2)