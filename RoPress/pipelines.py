# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb.cursors
from twisted.enterprise import adbapi

from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from scrapy.utils.project import get_project_settings
from scrapy import log
from datetime import datetime
import time
SETTINGS = get_project_settings()

class MySQLPipeline(object):

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.stats)

    def __init__(self, stats):
        #Instantiate DB
        self.dbpool = adbapi.ConnectionPool ('MySQLdb',
            host=SETTINGS['DB_HOST'],
            user=SETTINGS['DB_USER'],
            passwd=SETTINGS['DB_PASSWD'],
            port=SETTINGS['DB_PORT'],
            db=SETTINGS['DB_DB'],
            charset='utf8',
            use_unicode = True,
            cursorclass=MySQLdb.cursors.DictCursor
        )
        self.stats = stats
        dispatcher.connect(self.spider_closed, signals.spider_closed)
    def spider_closed(self, spider):
        """ Cleanup function, called after crawing has finished to close open
            objects.
            Close ConnectionPool. """
        self.dbpool.close()
    print "ok"
    def insert_record(self, tx, item):
        tx.execute(
            "SELECT link from press where data = '%s' and county = '%s' and press = '%s'" % (item['date'], item['county'], item['press']))
        links = [elem['link'] for elem in tx.fetchall()]
        if item['link'] not in links:
            
            result = tx.execute(
                "INSERT INTO press (title, textul, press, county, city, category, link, data) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (item['title'], item['text'], item['press'], item['county'], item['city'], item['category'], item['link'], item['date']))
            
            if result > 0:
                self.stats.inc_value('database/items_added')
        else:
            pass

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self.insert_record, item)
        query.addErrback(self._handle_error)
        return item

    def _handle_error(self, e):
		log.err(e)