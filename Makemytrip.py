import threading
from bs4 import BeautifulSoup as bsm
import time as tymme
import lxml
import urllib2, cookielib, urllib
import random
import json
import sys 
import re
import datetime as dat
from datetime import date, time, timedelta, datetime
import time as t
from random import randint
from datetime import timedelta as tde
import pickle
from dateutil.rrule import rrule, DAILY
import subprocess
import os


BASE_URL="http://flights.makemytrip.com/makemytrip/"

verification = []



def printit():
    threading.Timer(600.0, printit).start()

    site = 'https://free-proxy-list.net/'
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(site,headers=hdr) 
    url = urllib2.urlopen(req).read() 
    html = bsm(url,"lxml")                
    rows = html.findAll("tr") 
    global proxies_ips 
    global ips 
   
    proxies = []
    proxies_ips = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text for ele in cols]
        try:
            ipaddr = cols[0]       
            portNum = cols[1] 
            if portNum == str(80) :

                proxy = ipaddr+":"+portNum 
                portName = cols[6]    
                anonymity = cols[4]
                if anonymity == "anonymous" or anonymity == "elite proxy" :

                    last_checked = cols[7]
                    if portName == "no":
                        proxies_ips.append(str(proxy))
                        proxies.append(str(proxy)+" -> http" + "--" + str(anonymity) + "--" + str(last_checked)) 
                    else:
                        proxies_ips.append(str(proxy))
                        proxies.append(str(proxy)+" -> https"+ "--" + str(anonymity) + "--" + str(last_checked))
                else :
                    pass
            else :
                pass
        except:
            pass
    proxies_ips = proxies_ips[:20]       
    dummy_list = []
    for pqr in proxies_ips :
        pqr = pqr[:-3]
        dummy_list.append(pqr)




    ips = dummy_list
    print ips
printit()

print ips



random_ip = random.choice(ips)
while random_ip in verification :
	random_ip = random.choice(ips)
print "Picking first random IP"
print "verification length --" + str(len(verification)) 
verification.append(random_ip)
print random_ip


class MakeMyTrip(object):

    
    def __init__(self):
        self.url_browse = ""
        self.flights_data = ""
        self.stoppage = ""
        self.arrival_time = ""
        self.trip_json = []
        
    def browse(self, url="", roundtrip=False):
        print url
        tries = 1
        proxy_try = 1
        global random_ip
        global verification


        for attempt in range(1000) :
        	try :

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

		        hdr6 = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
		               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
		               'Accept-Encoding': 'none',
		               'Accept-Language': 'en-US,en;q=0.8',
		               'Connection': 'keep-alive'}

		        hdr = random.choice([hdr1, hdr2, hdr3, hdr4, hdr5, hdr6])

		        # print hdr

		        req = urllib2.Request(url, headers=hdr)

		        cj = cookielib.CookieJar()

		        
		        

		        for attrirt in range(10000) :
		        	try:
		        		proxy = urllib2.ProxyHandler({'http': random_ip})
		        		self.url_browse = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj), proxy).open(req,timeout=20).read()
		        		print "content extraction successful" 
                        

		        	except urllib2.HTTPError:  
		        		print 'There was an ERROR'
		        		print proxy_try
		        		if proxy_try > 4 :
		        			random_ip = random.choice(ips)
		        			while random_ip in verification :
		        				random_ip = random.choice(ips)
		        			print "loop executed during failed proxy try attempt"
		        			verification.append(random_ip)
		        			print random_ip + "-----url opening error"
		        			proxy_try = 1
		        		else :
		        			proxy_try = proxy_try + 1
		        	else :
		        		break
		        else :
		        	print "SOS I Repeat SOS, only GOD can help now"


		        fil = open("out.txt","w")
		        fil.write(self.url_browse)
		        fil.close()
		        i = 0
		        fil = open("out.txt","r")
		        if roundtrip:
		            json_list = json.loads(fil.read())
		            #print json_list#['filterData']
		            print "-"*50
		            json_list = json.loads(json_list['fd'])
		            return json_list
		        for line in fil.readlines():
		            i = i+1
		            if "flightsData" in line:
		                self.flights_data = line
		                break
		        temp_flights_data = self.flights_data.replace("var flightsData = ","").strip()
		        temp_flights_data = temp_flights_data[:-1]
		        fil = open("out.txt","w")
		        fil.write(temp_flights_data)
		        fil.close()
		        try :
		            json_list = json.loads(temp_flights_data)
		        except ValueError : 
		            json_list = 1
		        return json_list
        	except :


		    	print tries

		    	if tries > 3 :

		    		random_ip = random.choice(ips)
		    		while random_ip in verification :
		    			random_ip = random.choice(ips)
		    		print "loop executed"
		    		verification.append(random_ip)
		    		tries = 1
		    		print random_ip + " ---ip connection error"
		    	else :
		    		tries = tries + 1
        	else :
		    	break 
        else :

			failing = 'Failed_loading_from -- ' + str(url)
			print failing



    
    def create_json_oneway(self, dump_list):
        for i in range(len(dump_list)):
            temp = '{ "airline" : "' + dump_list[i]['le'][0]['an'] + '"'
            temp = temp + ', "price" : "' + str(dump_list[i]['af']) + '"'
            temp = temp + ', "total_time" : "' + str(dump_list[i]['td']) + '"'
            temp = temp + ', "depart_date" : "' + str(dump_list[i]['le'][0]['fd']) + '"'
            temp = temp + ', "depart_time" : "' + str(dump_list[i]['le'][0]['fdt']) + '"'
            temp_dump_list = dump_list[i]['le']
            for x in range(len(temp_dump_list)):
                if x == (len(temp_dump_list)-1):
                    temp = temp + ', "arrival_date" : "' + str(temp_dump_list[x]['fa']) + '"'
                    temp = temp + ', "arrival_time" : "' + str(temp_dump_list[x]['fat']) + '"}'
            self.trip_json.append(temp)
        return json.dumps(self.trip_json)
        
    def create_json_roundtrip(self, dump_list):
        #Todo : Complete this function to return the custom JSON as response 
        for i in range(len(dump_list)):
            return json.loads(['fd'])
        
    def journey_oneway(self, origin, destination, depart_date, adult=1, children=0, infant=0):
        adult = str(adult) if adult >= 1 else "1"
        children = str(children) if children >= 1 else str(children)
        infant = str(infant) if infant >= 1 else str(infant)
        new_url = BASE_URL + "search/O/O/E/" + adult +"/" + children + "/" + infant + "/S/V0/" + origin + "_" + destination + "_" + depart_date
        return self.browse(new_url)
    
    def journey_roundtrip(self, origin, destination, depart_date, return_date, adult=1, children=0, infant=0):
        new_url = BASE_URL + 'splitRTDataService.json?classType=E&deptDate=' + depart_date + '&fltMap=&fromCity='+ origin + '&noOfAdlts=' + str(adult) + \
        '&noOfChd=' + str(children) + '&noOfInfnt=' + str(infant) + '&returnDate=' + return_date + '&toCity=' + destination + '&tripType=R&tripTypeDup=R'
        return self.browse(new_url, True)
        
    #Todo: Get rid of this method
    def read_line(self):
        flights_data=""
        i = 0
        fil = open("out.txt","r")
        for line in fil.readlines():
            i = i+1
            if "flightsData" in line:
                flights_data = line
        #print "Total lines",i
        self.format_flights_data(flights_data)
        #self.getFlightTable(flights_data)
        
    #Todo: Get rid of this method
    def format_flights_data(self, flights_data):
        new_flights_data = flights_data.replace("var flightsData = ","").strip()
        new_flights_data = new_flights_data[:-1]
        fil = open("out.txt","w")
        fil.write(new_flights_data)
        fil.close()
        d = new_flights_data
        li = json.loads(d)
        self.create_json_oneway(li)
        #print type(new_flights_data)
            
    def get_extra_detail(self, flights_data):
        #date_size=len(flights_data)
        halt = flights_data[0]['f']
        layover = ""
        for x in range(len(flights_data)):
            halt = halt + u"   \u2708   " + flights_data[x]['t'] + " ( " + flights_data[x]['du'] + " )"
            if x > 0:
                layover = layover + flights_data[x]['f'] + "  ( " + flights_data[x]['lo'] + " )  "
            if x == (len(flights_data)-1):
                self.arrival_time = flights_data[x]['fa'] + " " +flights_data[x]['fat']
        print halt
        return layover
        #return halt
        
    def print_json(self, l):
        
        tmp_size = len(l)
        for i in range(tmp_size):   
            print ""
            print u"\033[1m" + l[i]['le'][0]['an'] , u"\033[0m      \u20B9 \033[92m", l[i]['af'], "\033[0m  in  ", l[i]['td']
            layover=self.get_extra_detail(l[i]['le']) 
            #ToDo
            print l[i]['le'][0]['fd'],  l[i]['le'][0]['fdt'], \
             u"  --->>  ", self.arrival_time
            print "\tStoppage : ", layover
            #print "Arrival : ", l[i]['le'][0]['fa'], l[i]['le'][0]['fat']
            print u"\u2982"*50

 
 #To write the required files into json format

    def file_json(self,l,destination, origin , flight_date):
        if l == 1 :
            taken_date = str(datetime.today().date())
            f1.write("Origin" + "," + "Destination" + "," + "Dept_Date" + "," + "Dept_Time" + "," + "Arr_Time" + "," + "Total_Fare" + "," + "Base_Fare" + "," + "Fuel_Fare" + "," + "Airways" + "," + "Available" + "," + "Duration" + "," + "Class_Type" + "," + "Flight Number" + "," + "Flight Code" + "," + "FlightID" + "," + "Hopping" + "," +"Taken" +"\n")
            f1.write(origin + "," + destination + "," + flight_date + "," + "NA" + "," + "NA" + "," + "NA" + "," + "NA" + "," + "NA" + "," + "NA" + "," + "NA" + "," + "NA" + "," + "NA" + ","+ "NA" + "," + "NA" + "," + "NA" + "," + "NA" + ","+ taken_date +"\n")
        else :
            tmp_size = len(l)
            f1.write("Origin" + "," + "Destination" + "," + "Dept_Date" + "," + "Dept_Time" + "," + "Arr_Time" + "," + "Total_Fare" + "," + "Base_Fare" + "," + "Fuel_Fare" + "," + "Airways" + "," + "Available" + "," + "Duration" + "," + "Class_Type" + "," + "Flight Number"+ "," + "Flight Code" + "," + "FlightID" + "," + "Hopping" + "," +"Taken" +"\n")
            for i in range(tmp_size):  
                airways = l[i]['le'][0]['an'] 
                fare = l[i]['af']
                deptdate = l[i]['le'][0]['dep']
                depttime = l[i]['le'][0]['fdt']
                arrtime = l[i]['le'][0]['fat']
                avail = l[i]['le'][0]['flightFare']['bookingClass']['availability']
                basefare = l[i]['le'][0]['flightFare']['baseFare']
                fuel_surcharge = l[i]['le'][0]['flightFare']['fuelSurcharge']
                duration = l[i]['td']
                origin = l[i]['le'][0]['o']
                desti = l[i]['le'][0]['d']
                class_type = l[i]['le'][0]['cls']
                flight_number = l[i]['le'][0]['fn']
                flight_code = l[i]['le'][0]['oc']
                Flight_ID = l[i]['fi']
                hopping = l[i]['hff']

                '''
                if hopping == True :
                    arrtime = l[i]['le'][1]['fat']
                else :
                    arrtime = l[i]['le'][0]['fat']
                '''
                taken_date = str(datetime.today().date())
                
                f1.write(origin + "," + desti + "," + deptdate + "," + depttime + "," + arrtime + "," + str(fare) + "," + str(basefare) + "," + str(fuel_surcharge) + "," +airways+ "," + avail + ","+duration + "," + class_type + ","+ flight_number + "," + flight_code + ","  + Flight_ID + "," + str(hopping) + "," +taken_date+  "\n")
                


# ["IDR","BBI","CJB","NAG","SXR","JAI","LKO","TRV","PNQ","GOI","AMD","COK","HYD","CCU","BLR","MAA","BOM","DEL"]
#['DEL', 'BOM', 'MAA', 'BLR', 'CCU', 'HYD', 'COK', 'AMD', 'GOI', 'PNQ', 'TRV', 'LKO', 'JAI', 'SXR', 'NAG', 'CJB', 'BBI', 'IDR']
# ['GOI', 'PNQ', 'TRV', 'LKO', 'JAI', 'NAG', 'CJB', 'BBI', 'IDR']
        
if __name__=="__main__":
    print "="*30 
    origins = ['GOI', 'PNQ', 'TRV', 'LKO', 'JAI', 'NAG', 'CJB', 'BBI', 'IDR']
    destinations = ['DEL', 'BOM', 'MAA', 'BLR', 'CCU', 'HYD', 'COK', 'AMD', 'GOI', 'PNQ', 'TRV', 'LKO', 'JAI', 'NAG', 'CJB', 'BBI', 'IDR']
    for origin in origins :
    	for destination in destinations :
    		if origin != destination :

    			#Range of dates in which we want the data
    			a = dat.date.today() + tde(days=1)
    			print a
    			b = a + tde(days=30)
    			print b
    			for dt in rrule(DAILY, dtstart=a, until=b):
					print dt.strftime("%d-%m-%Y")
					dept_date = str(dt.strftime("%d-%m-%Y"))
					bro = MakeMyTrip()
					f1=open('del1.csv', 'a') 
					bro.file_json(bro.journey_oneway(origin,destination,dept_date), destination, origin , dept_date)
					f1.close()
			else:
				pass
    print "Execution completed"	
    os.system('spd-say "Execution completed"')
   