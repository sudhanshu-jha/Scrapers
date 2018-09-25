# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from amazon.items import BookItem
from re import findall

class AmazonPipeline(object):
    def process_item(self, item, spider):
        item = self.__model_date__(item)
        return item

    def __model_date__(self, item):
        if('date_scraping' in item):
            item['date_scraping'] = item['date_scraping'].strftime(r"%d/%m/%Y")
        return item

class BooksPipeline(object):
    months = {
        'jan': '01',
        'fev': '02',
        'mar': '03',
        'abr': '04',
        'mai': '05',
        'jun': '06',
        'jul': '07',
        'ago': '08',
        'set': '09',
        'out': '10',
        'nov': '11',
        'dez': '12'
    }

    def process_item(self, item, spider):
        if('year_pub' in item):
            item['year_pub'] = self.__model_year_pub__(item['year_pub'])
        return item

    def __model_year_pub__(self, year_pub):
        day = findall(r"(\d+) [a-z]{3} \d+", year_pub)
        year = findall(r"\d+ [a-z]{3} (\d+)", year_pub)
        for month in self.months.keys():
            if(month in year_pub):
                print(year_pub)
                month = self.months[month]
                break
        if(day and year and month):
            day = day.pop()
            if(len(day)<2):
                day = '0' + str(day)
            return "{}/{}/{}".format(day, month, year.pop())
        return year_pub


