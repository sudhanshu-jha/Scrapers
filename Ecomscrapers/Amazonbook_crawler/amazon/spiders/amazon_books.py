# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from scrapy.loader import ItemLoader
from amazon.items import BookItem
from scrapy.loader.processors import MapCompose
from datetime import datetime


class AmazonBooksSpider(Spider):
    name = 'amazon_books'
    allowed_domains = ['amazon.com.br']
    start_urls = [
        'https://www.amazon.com.br/Livros/b/ref=nav__books_all?ie=UTF8&node=6740748011']

    def parse(self, response):
        categories = response.xpath(
            "//span[@class='a-button a-button-span12 bxc-button  bxc-grid__button--light']//a/@href")
        for category in categories.extract():
            yield Request(response.urljoin(category), callback=self.parse_categories)

    def parse_categories(self, response):
        next_page = response.xpath("//a[@id='pagnNextLink']/@href").extract()
        if(next_page):
            yield Request(response.urljoin(next_page.pop()), callback=self.parse_categories)

        books = response.xpath(
            "//a[@class='a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal']/@href")
        for book in books.extract():
            yield Request(book, callback=self.parse_book)

    def parse_book(self, response):
        book = ItemLoader(item=BookItem(), response=response)
        book.add_xpath('title', "//span[@id='productTitle']/text()")
        book.add_xpath(
            'lang', "//h1[@id='title']/span[2]/text()", re=r"\((\w+)\)")
        book.add_xpath('authors', "//span[@class='author notFaded']/a/text()")
        book.add_xpath(
            'year_pub', "//h1[@id='title']//span//text()", re=r"\d{1,2} [a-z]{3} \d{4}")
        book.add_xpath(
            'pages', "//div[@class='content']//li[1]/text()", re=r"\d+")
        book.add_xpath(
            'pub_house', "//div[@class='content']//li[2]/text()", re=r"([\w _]+);")
        book.add_xpath('details', "normalize-space(.//div[@class='content'])")
        book.add_xpath('price', "//div[@id='soldByThirdParty']/span/text()")
        book.add_xpath('images', "//div[@id='main-image-container']//img/@src")
        book.add_xpath(
            'edition', "normalize-space(.//div[@class='content'])", re=r"Edição:([\w \d]+)\(")
        book.add_xpath(
            'rating', "normalize-space(.//div[@class='content'])", re=r"(\d.\d) de 5")
        book.add_xpath(
            'rating_count', "//span[@id='acrCustomerReviewText']/text()", re=r"\d+")

        book.add_value('andress_url', response.url)
        book.add_value('date_scraping', datetime.now())
        yield book.load_item()
