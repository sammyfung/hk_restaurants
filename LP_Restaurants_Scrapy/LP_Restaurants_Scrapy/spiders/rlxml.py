# -*- coding: utf-8 -*-
import scrapy
from LP_Restaurants_Scrapy.items import CafescrapItem

class RlxmlSpider(scrapy.Spider):
  name = "rlxml"
  allowed_domains = ["fehd.gov.hk"]
  start_urls = (
    'http://www.fehd.gov.hk/english/licensing/license/text/LP_Restaurants_EN.XML',
  )

  def parse(self, response):
    lics = response.xpath('//LPS/LP')
    for lic in lics:
      item = CafescrapItem()
      item['type'] = lic.xpath('TYPE/text()')[0].extract()
      item['district'] = lic.xpath('DIST/text()')[0].extract()
      item['num'] = lic.xpath('LICNO/text()')[0].extract()
      item['name'] = lic.xpath('SS/text()')[0].extract()
      item['address'] = lic.xpath('ADR/text()')[0].extract()
      try: 
        item['addition'] = lic.xpath('INFO/text()')[0].extract()
      except IndexError:
        item['addition'] = ''
      item['expire_date'] = lic.xpath('EXPDATE/text()')[0].extract()
      yield item
