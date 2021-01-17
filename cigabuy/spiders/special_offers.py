# -*- coding: utf-8 -*-
import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['www.cigabuy.com']
    start_urls = ['https://www.cigabuy.com/specials.html']

    def parse(self, response):
        for product in response.xpath("//ul[@class ='productlisting-ul']/div/div"):
            
            yield{
                'title' : product.xpath(".//a[@class = 'p_box_title']/text()").get(),
                #using urljoin as the url is relative.
                'url' : response.urljoin(product.xpath(".//a[@class = 'p_box_title']/@href").get()),
                'price' : product.xpath(".//div[@class = 'p_box_price cf']/text()").get(),
                
            }
