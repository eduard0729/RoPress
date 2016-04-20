# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import BaseSpider
from scrapy.selector import Selector
from RoPress.items          import RopressItem
from scrapy.http            import Request
import re
from urlparse import urlparse
import datetime


class BotosaninewsSpider(scrapy.Spider):
    name = "BotosaniNews"
    start_urls = ['http://botosaninews.ro/']

    luni = {
        'ianuarie' : '01',
        'februarie' : '02',
        'martie' : '03',
        'aprilie' : '04',
        'mai' : '05',
        'iunie' : '06',
        'iulie' : '07',
        'august' : '08',
        'septembrie' : '09',
        'octombrie' : '10',
        'noiembrie' : '11',
        'decembrie' : '12'
    }

    def parse(self, response):
        links = response.xpath('//div[@id="recent-news-block"]/div[@class="post-container clearfix"]/h2[@class="entry-title"]/a/@href').extract()
        titles = response.xpath('//div[@id="recent-news-block"]/div[@class="post-container clearfix"]/h2[@class="entry-title"]/a/text()').extract()
        dates = response.xpath('//div[@id="recent-news-block"]/div[@class="post-container clearfix"]/div[@class="entry-meta entry-header"]/span/text()').extract()
        for link, title, date in zip(links, titles, dates):
                item = RopressItem()
                item['link'] = link
                item['title'] = title
                item['county'] = 'Botosani'
                item['city'] = 'Botosani'
                item['press'] = 'BotosaniNews'
                item['date'] = date
                for x in self.luni:
                    item['date'] = item['date'].replace(x, self.luni[x])
                item['date'] = datetime.datetime.strptime(item['date'], '%d %m %Y')
                request = Request(link, callback=self.parse_fulldetail)
                request.meta['item'] = item
                yield request

    def parse_fulldetail(self, response):
        item = response.meta['item']
        item['category'] = response.xpath('//ul[@class="cat"]/li/a/text()').extract()
        item['category'] = " ".join(item['category'])
        item['text']= response.xpath('//div[@class="entry-content"]//text()').extract()
        item['text'] = " ".join(item['text'])
        item['text'] = item['text'].strip()
        yield item