 # -*- coding: utf-8 -*-

import os
import sys
import urllib,urllib2,cookielib
import datetime,time
import re
import random
from bs4 import BeautifulSoup as soup
import io


text_file = open("amazonreviewlinks.txt", "r")
lines = text_file.read().split(',')

no = len(lines)


#opening product link

print no
for hij in lines :

	Review_link_len = 0

	hdr1 = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	       'Accept-Encoding': 'none',
	       'Accept-Language': 'en-US,en;q=0.8',
	       'Connection': 'keep-alive'}
	hdr2 = {'User-Agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	       'Accept-Encoding': 'none',
	       'Accept-Language': 'en-US,en;q=0.8',
	       'Connection': 'keep-alive'}
	hdr3 = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)',
	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	       'Accept-Encoding': 'none',
	       'Accept-Language': 'en-US,en;q=0.8',
	       'Connection': 'keep-alive'}
	hdr4 = {'User-Agent': 'Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11',
	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	       'Accept-Encoding': 'none',
	       'Accept-Language': 'en-US,en;q=0.8',
	       'Connection': 'keep-alive'}
	hdr5 = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25',
	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	       'Accept-Encoding': 'none',
	       'Accept-Language': 'en-US,en;q=0.8',
	       'Connection': 'keep-alive'}

	while Review_link_len == 0 :
	  try :

	    hdr = random.choice([hdr1,hdr2,hdr3,hdr4,hdr5])

	    req = urllib2.Request(hij, headers=hdr)

	    cj = cookielib.CookieJar()

	    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	    response = opener.open(req,timeout=10)        
	    content = response.read()
	    response.close() 
	    page_soup = soup(content,"html.parser")   
	    site1 = page_soup.findAll("a",{"id" : "acrCustomerReviewLink"})
	    Review_link_len = len(site1)
	    print Review_link_len

	  except :
	    hdr = random.choice([hdr1,hdr2,hdr3,hdr4,hdr5])

	    req = urllib2.Request(hij, headers=hdr)

	    cj = cookielib.CookieJar()

	    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	    response = opener.open(req,timeout=10)        
	    content = response.read()
	    response.close() 
	    page_soup = soup(content,"html.parser")   
	    site1 = page_soup.findAll("a",{"id" : "acrCustomerReviewLink"})
	    Review_link_len = len(site1)
	    print Review_link_len

	  

	site2 = site1[0]['href']
	amazon_homepage = "https://www.amazon.in"
	site = amazon_homepage + site2
	print site 


	#openinig review link


	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	       'Accept-Encoding': 'none',
	       'Accept-Language': 'en-US,en;q=0.8',
	       'Connection': 'keep-alive'}
	len_captcha = 0
	while len_captcha == 0 :
		try :
			req = urllib2.Request(site, headers=hdr)
			cj = cookielib.CookieJar()
			opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
			response = opener.open(req,timeout = 10)
			content = response.read()				
			response.close()

			page_soup = soup(content,"html.parser")
			review_element = page_soup.findAll("div",{"class" : "a-section celwidget"})
			captcha = page_soup.findAll("li",{"class" : "a-last"})
			len_captcha = len(captcha)

		except :
			req = urllib2.Request(site, headers=hdr)
			cj = cookielib.CookieJar()
			opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
			response = opener.open(req,timeout = 10)
			content = response.read()				
			response.close()

			page_soup = soup(content,"html.parser")
			review_element = page_soup.findAll("div",{"class" : "a-section celwidget"})
			captcha = page_soup.findAll("li",{"class" : "a-last"})
			len_captcha = len(captcha)


	next_button1 = page_soup.findAll("li",{"class" : "a-last"})[0]
	next_button = next_button1.findAll("a")
	next_button_len = len(next_button)
	if next_button_len == 0 :
		next_button_len = 50 
	else :
		next_button = next_button1.findAll("a")[0]['href']

	print len(next_button)
	try :

		filename = page_soup.findAll("a",{"class" : "a-link-normal"})[0].text.strip()
		#filename = filename.replace('\'', "!")
		filename = filename + '.csv'
		f = io.open(filename,"w",encoding="utf-8")
		headers = "Customer name,Customer ratings out of 5.0,Review date,Review word count,Customer review\n"
		f.write(unicode(headers,"utf-8"))

	except :

		filename = page_soup.findAll("a",{"class" : "a-link-normal"})[0].text.strip()[:10]
		#filename = filename.replace('\'', "!")
		filename = filename + '.csv'
		f = io.open(filename,"w",encoding="utf-8")
		headers = "Customer name,Customer ratings out of 5.0,Review date,Review word count,Customer review\n"
		f.write(unicode(headers,"utf-8"))

	#loop for content extraction

	while next_button_len != 50 :
		for single in review_element :
			
			try :
				review007 = single.findAll("span",{"data-hook" : "review-body"})[0].getText()
				review007 = review007.replace(",", "|")
				review007 = len(review007.split())
				review = single.findAll("span",{"data-hook" : "review-body"})[0].getText()
				review = (review.encode('utf-8', 'ignore')).encode("utf-8",errors='ignore')
				review = unicode(review,"utf-8",errors='ignore')
				review = review.replace(",", "|")
				print review
				
			except :	
				review = "can not extract review"


			try :
				ratings = single.findAll("a",{"class" : "a-link-normal"})[0]['title'][:3]
				ratings = (ratings.encode('utf-8', 'ignore')).encode("utf-8",errors='ignore')
				ratings = unicode(ratings,"utf-8",errors='ignore')
				ratings = ratings.replace(",", "|")
				print ratings
			except :	
				ratings = "can not extract ratings"


			try :
				review_date = single.findAll("span",{"class" : "a-size-base a-color-secondary review-date"})[0].getText()[3:]
				review_date = (review_date.encode('utf-8', 'ignore')).encode("utf-8",errors='ignore')
				review_date = unicode(review_date,"utf-8",errors='ignore')
				review_date = review_date.replace(",", "|")
				print review_date
			except :	
				ratings = "can not extract review date"

			try :
				
				review_length = unicode(review007)
				print review_length
			except :	
				review_length = "can not extract review length"


			try :
				customer_name = single.findAll("a",{"data-hook" : "review-author"})[0].getText().strip()
				customer_name = (customer_name.encode('utf-8', 'ignore')).encode("utf-8",errors='ignore')
				customer_name = unicode(customer_name,"utf-8",errors='ignore')
				customer_name = customer_name.replace(",", "|")
				print customer_name	
			except :
				customer_name = "can not extract customer name"
			data1 = [customer_name , ratings, review_date, review_length, review]
			data1 = customer_name + "," + ratings + "," + review_date + "," + review_length + ","  + review + "\n" 
			try :
				f.write(data1)
			except :
				data1 = unicode("can not find customr name") + "," + unicode("can not extract review") + "\n"
				f.write(data1)


		next_button1 = page_soup.findAll("li",{"class" : "a-last"})[0]
		next_button = next_button1.findAll("a")
		next_button_len = len(next_button)
		
		if next_button_len == 0 :
			next_button_len = 50 
		else :
			next_button = next_button1.findAll("a")[0]['href']
		
		

		try :
			amazon_homepage = "https://www.amazon.in"
			site = amazon_homepage + next_button
			
		except :
			site = 0
		print site
		if site == 0 :
			next_button_len = 50

		else :
			try :
				try : 
					
					req = urllib2.Request(site, headers=hdr)
					cj = cookielib.CookieJar()
					cj.clear_session_cookies()
					opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
					response = opener.open(req,timeout = 10)
					content = response.read()				
					response.close()

					page_soup = soup(content,"html.parser")
					review_element = page_soup.findAll("div",{"class" : "a-section celwidget"})

					captcha = page_soup.findAll("li",{"class" : "a-last"})
					len_captcha = len(captcha)
					while len_captcha == 0 :
						cj.clear_session_cookies()
						req = urllib2.Request(site, headers=hdr)
						cj = cookielib.CookieJar()
						opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
						response = opener.open(req,timeout = 10)
						content = response.read()				
						response.close()

						page_soup = soup(content,"html.parser")
						review_element = page_soup.findAll("div",{"class" : "a-section celwidget"})
						captcha = page_soup.findAll("li",{"class" : "a-last"})
						len_captcha = len(captcha)
				except :
					
					req = urllib2.Request(site, headers=hdr)
					cj = cookielib.CookieJar()
					cj.clear_session_cookies()
					opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
					response = opener.open(req,timeout = 10)
					content = response.read()				
					response.close()

					page_soup = soup(content,"html.parser")
					review_element = page_soup.findAll("div",{"class" : "a-section celwidget"})	



					captcha = page_soup.findAll("li",{"class" : "a-last"})
					len_captcha = len(captcha)
					while len_captcha == 0 :
						cj.clear_session_cookies()
						req = urllib2.Request(site, headers=hdr)
						cj = cookielib.CookieJar()
						opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
						response = opener.open(req,timeout = 10)
						content = response.read()				
						response.close()

						page_soup = soup(content,"html.parser")
						review_element = page_soup.findAll("div",{"class" : "a-section celwidget"})
						captcha = page_soup.findAll("li",{"class" : "a-last"})
						len_captcha = len(captcha)
			except :
				
				print "sleeping due to connection errors"
				try : 

					req = urllib2.Request(site, headers=hdr)
					cj = cookielib.CookieJar()
					cj.clear_session_cookies()
					opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
					response = opener.open(req,timeout = 10)
					content = response.read()				
					response.close()

					page_soup = soup(content,"html.parser")
					review_element = page_soup.findAll("div",{"class" : "a-section celwidget"})




					captcha = page_soup.findAll("li",{"class" : "a-last"})
					len_captcha = len(captcha)
					while len_captcha == 0 :
						cj.clear_session_cookies()
						req = urllib2.Request(site, headers=hdr)
						cj = cookielib.CookieJar()
						opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
						response = opener.open(req,timeout = 10)
						content = response.read()				
						response.close()

						page_soup = soup(content,"html.parser")
						review_element = page_soup.findAll("div",{"class" : "a-section celwidget"})
						captcha = page_soup.findAll("li",{"class" : "a-last"})
						len_captcha = len(captcha)

				except :
					
					print "sleeping due to connection error"
					req = urllib2.Request(site, headers=hdr)
					cj = cookielib.CookieJar()
					cj.clear_session_cookies()
					opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
					response = opener.open(req,timeout = 10)
					content = response.read()				
					response.close()

					page_soup = soup(content,"html.parser")
					review_element = page_soup.findAll("div",{"class" : "a-section celwidget"})

					captcha = page_soup.findAll("li",{"class" : "a-last"})
					len_captcha = len(captcha)
					while len_captcha == 0 :
						cj.clear_session_cookies()
						req = urllib2.Request(site, headers=hdr)
						cj = cookielib.CookieJar()
						opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
						response = opener.open(req,timeout = 10)
						content = response.read()				
						response.close()

						page_soup = soup(content,"html.parser")
						review_element = page_soup.findAll("div",{"class" : "a-section celwidget"})
						captcha = page_soup.findAll("li",{"class" : "a-last"})
						len_captcha = len(captcha)
	f.close()
