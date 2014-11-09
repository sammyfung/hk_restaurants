# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CafescrapItem(scrapy.Item):
  type = scrapy.Field()
  district = scrapy.Field()
  num = scrapy.Field()
  name = scrapy.Field()
  address = scrapy.Field()
  addition = scrapy.Field()
  expire_date = scrapy.Field()
 
