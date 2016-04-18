# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders             import BaseSpider
from scrapy.selector import Selector
from RoPress.items          import RopressItem
from scrapy.http            import Request
import re
from urlparse import urlparse
import datetime

class SuceavanewsSpider(scrapy.Spider):
    name = "SuceavaNews"
    start_urls = (
        'http://www.suceavanews.ro/',
    )

    def parse(self, response):
		links = response.xpath('//div[@id="recent-news-block"]/div[@class="post-container clearfix"]/h2[@class="entry-title"]/a/@href').extract()
		titles = response.xpath('//div[@id="recent-news-block"]/div[@class="post-container clearfix"]/h2[@class="entry-title"]/a/text()').extract()
		dates = response.xpath('//div[@id="recent-news-block"]/div[@class="post-container clearfix"]/div[@class="entry-meta entry-header"]/span/text()').extract()
		for link, title, date in zip(links, titles, dates):
			item = RopressItem()
          	item['link'] = link
          	title = title.encode(encoding='UTF-8',errors='strict')
          	item['title'] = title
          	item['county'] = 'Suceava'
          	item['city'] = 'Suceava'
          	item['press'] = 'SuceavaNews'
          	request = Request(link, callback=self.parse_fulldetail)
          	request.meta['item'] = item
          	yield request   
    
    def parse_fulldetail(self, response):
        item = response.meta['item']
        item['category'] = response.xpath('//ul[@class="cat"]/li/a/text()').extract()
        item['category'] = " ".join(item['category'])
        item['text']= response.xpath('//div[@class="entry-content"]//text()').extract()
        item['text'] = " ".join(item['text'])
        yield item

