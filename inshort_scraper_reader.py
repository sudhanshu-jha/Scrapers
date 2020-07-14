# A simple python code for scraping the web of news site ex:inshorts.com/en/read and giving the news head lines as voice message and in message boxes in ubuntu.

#required packages : BeautifulSoup, espeak.

#import the required packages.
from urllib import urlopen       # Open url using urlopen
from bs4 import BeautifulSoup    # Import BeautifulSoup for scraping.
import subprocess		
import os
from time import sleep
import re


def sendmessage(message):        # This function is used for notifing the news.
    subprocess.Popen(['notify-send', message])
    return

sendmessage("Hello Boss.")
sendmessage("Reading News for you!")

html = urlopen("https://inshorts.com/en/read")       #open the url using urlopen.
bsObj = BeautifulSoup(html.read(),"html.parser")     # get the beautiful soup object after parsing the html page
News_headlines = bsObj.find_all('div', attrs={'itemprop':'articleBody'})   #finding in the html page all the divs with item propertie as articleBody
sleep(2)
sendmessage("Inshorts News will be read in 3 seconds")
sleep(2)

for x in News_headlines:
	st=x.string
	news=""
	st=st.encode('utf8','ignore')		     #encode the string as utf8
	regex = re.compile('[^.,a-zA-Z\w\s]'+'')     #regular expression to get the text out of the News_headlines string 'st'.
	news=regex.sub(' ',st)           
	news= "espeak "+ "'"+news+"'"+"  -s 100"     #create the command for reading the news using espeak module.
	print(news)
	os.system(news)	                             #execute the command of espeak. 
	sleep(2)				     #wait for 3 seconds for reading the second news

# An simple addition can be using a while loop and get the page after 60 minutes for latest news.
# Other modifications can be like using another web page to be scraped and accordingly get the headlines.
