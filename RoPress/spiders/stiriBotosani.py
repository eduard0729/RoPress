# -*- coding: utf-8 -*-
import scrapy
from scrapy.spider             import BaseSpider
from scrapy.selector import Selector
from RoPress.items          import RopressItem
from scrapy.http            import Request
import re
from urlparse import urlparse
import datetime


class StiribotosaniSpider(scrapy.Spider):
    name = "stiriBotosani"
    start_urls = ['http://www.stiri.botosani.ro/']

    def parse(self, response):
        links = response.xpath('//div[@class="col_a"]/div[@class="box"][2]/div[@class="box_01"]/span/h3/a/@href').extract()
        titles = response.xpath('//div[@class="col_a"]/div[@class="box"][2]/div[@class="box_01"]/span/h3/a/text()').extract()
        dates = response.xpath('//div[@class="col_a"]/div[@class="box"][2]/div[@class="box_01"]/div[@class="box_meniu"]/ul/li[@class="FR"]/a/text()').extract()
        for link, title, date in zip(links, titles, dates):
            try:
                if (datetime.datetime.strptime(date, '%I:%M')):
                    item = RopressItem()
                    link = 'http://stiri.botosani.ro' + link
                    item['link'] = link
                    item['title'] = title.strip()
                    item['county'] = 'Botosani'
                    item['city'] = 'Botosani'
                    item['press'] = 'Stiri.Botosani'
                    request = Request(link, callback=self.parse_fulldetail)
                    request.meta['item'] = item
                    yield request   
            except ValueError:
                pass

    def parse_fulldetail(self, response):
        item = response.meta['item']
        item['category'] = response.xpath('//div[@class="col_a"]/div[@class="box_artikle"]/h2/text()').extract()
        item['category'] = " ".join(item['category'])
        item['text']= response.xpath('//div[@class="col_a"]/div[@class="box_artikle"]/div[@class="box_01"]/*[not(@class="socialcontainer" or @class="fb-like fb_iframe_widget" or @class="stireh3" or a[@target="_new"] or @style="font-size:11px; border-top: 1px #ccc solid; border-bottom: 1px #ccc solid; width: 94%; margin: 5px 5px 0 5px;") ]//text()').extract()
        item['text'] = " ".join(item['text'])
        item['text'] = item['text'].strip()
        yield item