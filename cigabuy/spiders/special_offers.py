# -*- coding: utf-8 -*-
import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['www.cigabuy.com/specials.html']
    start_urls = ['http://www.cigabuy.com/specials.html/']

    def parse(self, response):
        pass
