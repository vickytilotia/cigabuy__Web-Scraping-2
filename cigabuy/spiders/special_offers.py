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
                'discounted_price' : product.xpath(".//div[@class = 'p_box_price cf']/span[1]/text()").get(),
                'original_price' : product.xpath(".//div[@class = 'p_box_price cf']/span[2]/text()").get()
                
            }
        # extracting next pages
        next_page = response.xpath("//a[@class='nextPage']/@href").get()

        #check if the next page is exist or not!
        if next_page:
            yield scrapy.Request(url = next_page, callback=self.parse)
