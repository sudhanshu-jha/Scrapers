# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from scrapy.loader.processors import TakeFirst, Join


class BookItem(Item):
    title = Field(output_processor=TakeFirst())
    lang = Field(output_processor=TakeFirst())
    authors = Field()
    year_pub = Field(output_processor=TakeFirst())
    pages = Field(output_processor=TakeFirst())
    pub_house = Field(output_processor=TakeFirst())
    details = Field(output_processor=Join())
    price = Field(output_processor=TakeFirst())
    images = Field()
    edition = Field(output_processor=TakeFirst())
    rating = Field(output_processor=TakeFirst())
    rating_count = Field(output_processor=TakeFirst())

    andress_url = Field(output_processor=TakeFirst())
    date_scraping = Field(output_processor=TakeFirst())
