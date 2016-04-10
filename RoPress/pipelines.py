# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
import MySQLdb
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request

class MySQLStorePipeline(object):
  def __init__(self):
    self.conn = MySQLdb.connect(user='admin_root', passwd='tekit2016', db='admin_press', host='104.238.188.243', charset="utf8", use_unicode=True)
    self.cursor = self.conn.cursor()

def process_item(self, item, spider):    
    try:
    	print ok
    	self.cursor.execute("""INSERT INTO press (title, press, text, link, county, category, date, city) VALUES (%s, %s, %s, %s, %s, %s, %s)""", (item['title'].encode('utf-8'), item['press'].encode('utf-8'),  item['text'].encode('utf-8'), item['link'].encode('utf-8'), item['county'].encode('utf-8'), item['category'].encode('utf-8'),  item['date'].encode('utf-8'), item['city'].encode('utf-8')))

    	self.conn.commit()


    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])


    return item