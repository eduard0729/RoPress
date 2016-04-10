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
		result = tx.execute(
			""" INSERT INTO press VALUES (title, press, textul, link, county, data, city) VALUES (%s, %s, %s, %s, %s, %s, %s)""", (item['title'].encode('utf-8'), item['press'].encode('utf-8'),  item['text'], item['link'].encode('utf-8'), item['county'],  datetime.today(), item['city']))
		if result > 0:
			self.stats.inc_value('database/items_added')

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self.insert_record, item)
        query.addErrback(self._handle_error)
        return item
	


	def _handle_error(self, e):
		log.err(e)