# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders             import BaseSpider
from scrapy.selector import Selector
from RoPress.items          import RopressItem
from scrapy.http            import Request
import re
from urlparse import urlparse
import datetime
import urllib2
import unicodedata


class AdevarulSpider(scrapy.Spider):
    name = "adevarul"
    start_urls = [
        'http://adevarul.ro/news/bucuresti/',
    ]
    judete=['satu-mare', 'baia-mare', 'zalau', 'oradea', 'bistrita', 'cluj-napoca', 'botosani','suceava','iasi','piatra-neamt','vaslui','bacau','arad','timisoara','hunedoara','resita','alba-iulia','sibiu','targu-mures','brasov','turnu-severin','targu-jiu','craiova','ramnicu-valcea','slatina','alexandria','pitesti','targoviste','ploiesti','giurgiu','calarasi','constanta','slobozia','braila','tulcea','galati','buzau','focsani']
    for x in judete:
      start_urls.append('http://adevarul.ro/locale/%s' % x + '/')
    jud = { 
      'Baia Mare': 'Maramureş',
      'Piatra Neamţ': 'Neamţ',
      'Oradea': 'Bihor',
      'Iaşi': 'Iaşi',
      'Suceava': 'Suceava',
      'Satu Mare': 'Satu-Mare',
      'Vaslui': 'Vaslui',
      'Sibiu': 'Sibiu',
      'Hunedoara': 'Hunedoara',
      'Reşiţa': 'Caraş Severin',
      'Cluj-Napoca': 'Cluj',
      'Bistriţa': 'Bistriţa-Năsăud',
      'Botoşani': 'Botoşani',
      'Târgu-Mureş': 'Mureş',
      'Alba Iulia': 'Alba',
      'Timişoara': 'Timiş',
      'Bacău': 'Bacău',
      'Zalău': 'Sălaj',
      'Craiova': 'Dolj',
      'Turnu-Severin': 'Mehedinţi',
      'Braşov': 'Braşov',
      'Slatina': 'Olt',
      'Alexandria': 'Teleorman',
      'Slobozia': 'Ialomiţa',
      'Tulcea': 'Tulcea',
      'Galaţi': 'Galaţi',
      'Târgu-Jiu': 'Gorj',
      'Brăila': 'Brăila',
      'Constanţa': 'Constanţa',
      'Călăraşi': 'Călăraşi',
      'Râmnicu Vâlcea': 'Vâlcea',
      'Giurgiu': 'Giurgiu',
      'Ploieşti': 'Prahova',
      'Târgovişte': 'Dâmboviţa',
      'Piteşti': 'Argeş',
      'Focşani': 'Vrancea',
      'Buzău': 'Buzău',
      'Bucureşti': 'Bucureşti',
      'Arad': 'Arad'
      } 

    def parse(self, response):

      if response.url == 'http://adevarul.ro/news/bucuresti/':

        titles = response.xpath('//article/h3[@class="defaultTitle"]/a/text()').extract()
        links = response.xpath('//article/h3[@class="defaultTitle"]/a/@href').extract()
        shortdescripts = response.xpath('//div[@class="article-text"]/p[@itemprop="description"]/text()').extract()
        judet = response.xpath('//span[@class="category-tag"]/a/text()').extract_first()
        judet = judet.encode(encoding='UTF-8',errors='strict')
        for title, shortdescript, link in zip(range(0, len(titles)), range(0, len(shortdescripts)), links):
          titles[title] = titles[title].encode(encoding='UTF-8',errors='strict')
          shortdescripts[shortdescript] = shortdescripts[shortdescript].encode(encoding='UTF-8',errors='strict')
          item = RopressItem()
          link = 'http://adevarul.ro' + link
          item['county'] = self.jud[judet]
          item['link'] = link.decode().encode('utf-8')
          item['city'] = judet
          item['title'] = titles[title]
          item['text'] = shortdescripts[shortdescript]
          item['press'] = 'Adevarul'
          request = Request(link, callback=self.parse_fulldetail)
          request.meta['item'] = item
          yield request

      else:
        titles = response.xpath('//article[@class="adv_blue"]/h3[@class="defaultTitle"]/a/text()').extract()
        links = response.xpath('//article[@class="adv_blue"]/h3[@class="defaultTitle"]/a/@href').extract()
        shortdescripts = response.xpath('//div[@class="article-text"]/p[@itemprop="about"]/text()').extract()
        judet = response.xpath('//span[@class="category-tag"]/a/text()').extract_first()
        judet = judet.encode(encoding='UTF-8',errors='strict')
        for title, shortdescript, link in zip(range(0, len(titles)), range(0, len(shortdescripts)), links):
          titles[title] = titles[title].encode(encoding='UTF-8',errors='strict')
          shortdescripts[shortdescript] = shortdescripts[shortdescript].encode(encoding='UTF-8',errors='strict')
          item = RopressItem()
          link = 'http://adevarul.ro' + link
          item['county'] = self.jud[judet]
          item['link'] = link.decode().encode('utf-8')
          item['city'] = judet
          item['title'] = titles[title]
          item['text'] = shortdescripts[shortdescript]
          item['press'] = 'Adevarul'
          request = Request(link, callback=self.parse_fulldetail)
          request.meta['item'] = item
          yield request  

    def parse_fulldetail(self, response):
        item = response.meta['item']
        item['category'] = 'no-cat'
        item['date'] = response.xpath('//time/@datetime').extract()
        item['date'] = " ".join(item['date'])
        item['date'] = datetime.datetime.strptime(item['date'], '%m-%d-%y')
        yield item