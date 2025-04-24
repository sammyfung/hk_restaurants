# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RestaurantItem(scrapy.Item):
  country = scrapy.Field()
  city = scrapy.Field()
  source = scrapy.Field()
  district = scrapy.Field()
  license_no = scrapy.Field()
  name = scrapy.Field()
  address = scrapy.Field()
  chinese_name = scrapy.Field()
  chinese_address = scrapy.Field()
  license_code = scrapy.Field()
  license_type = scrapy.Field()
  license_district = scrapy.Field()
  license_district_code = scrapy.Field()
  license_expiry_date = scrapy.Field()
  license_addition = scrapy.Field() 
  license_addition_code = scrapy.Field()
