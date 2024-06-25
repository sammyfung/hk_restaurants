# -*- coding: utf-8 -*-
import scrapy
from hk_restaurants.items import RestaurantItem

class FehdSpider(scrapy.Spider):
  name = "fehd"
  allowed_domains = ["fehd.gov.hk"]
  start_urls = (
    'http://www.fehd.gov.hk/english/licensing/license/text/LP_Restaurants_EN.XML',
  )
  LICENSE_CODE_TYPE = {
    'RL': 'General Restaurant Licence',
    'RR': 'Light Refreshment Restaurant Licence',
    'MR': 'Marine Restaurant Licence'
  }
  ADDITION_CODE_TYPE = {
    'A': 'Licensed restaurant with outside seating accommodation',
    'B': 'Licensed restaurant issued with karaoke establishment permit',
    'C': 'Licensed restaurant issued with karaoke establishment exemption order',
    'D': 'Licensed restaurant that are recognized by FEHD for the revised inspection regime after fully implemented the food safety system under ISO 22000 and obtained the ISO 22000 Certification',
    'E': 'Licensed restaurant approved to sell meat to be eaten in raw state for consumption on the premises',
    'F': 'Licensed restaurant approved to sell oyster to be eaten in raw state for consumption on the premises',
    'G': 'Licensed restaurant approved to sell sashimi for consumption on the premises',
    'H': 'Licensed restaurant approved to sell sushi for consumption on the premiseas'
  }
  DISTRICT_CODE = {
    '11': 'Eastern',
    '12': ' Wan Chai',
    '15': 'Southern',
    '17': 'Islands',
    '18': 'Central/Western',
    '51': 'Kwun Tong',
    '52': 'Kowloon City',
    '53': 'Wong Tai Sin',
    '61': 'Yau Tsim',
    '62': 'Mong Kok',
    '63': 'Sham Shui Po',
    '91': 'Kwai Tsing',
    '92': 'Tsuen Wan',
    '93': 'Tuen Mun',
    '94': 'Yuen Long',
    '95': 'Tai Po',
    '96': 'North',
    '97': 'Sha Tin',
    '98': 'Sai Kung'
  }

  def parse(self, response):
    lics = response.xpath('//LPS/LP')
    for lic in lics:
      item = RestaurantItem()
      item['country'] = 'HK'
      item['city'] = 'Hong Kong'
      item['source'] = 'FEHD HK'
      item['license_code'] = lic.xpath('TYPE/text()')[0].extract()
      item['license_type'] = self.LICENSE_CODE_TYPE[item['license_code']]
      item['license_district_code'] = lic.xpath('DIST/text()')[0].extract()
      item['license_district'] = self.DISTRICT_CODE[item['license_district_code']]
      item['license_no'] = lic.xpath('LICNO/text()')[0].extract()
      item['name'] = lic.xpath('SS/text()')[0].extract()
      item['address'] = lic.xpath('ADR/text()')[0].extract()
      try: 
        item['license_addition_code'] = lic.xpath('INFO/text()')[0].extract()
        item['license_addition'] = {}
        for code in item['license_addition_code'].split('#'):
          if code != '':
            item['license_addition']['#'+code] = self.ADDITION_CODE_TYPE[code]
      except IndexError:
        item['license_addition_code'] = ''
      item['license_expiry_date'] = lic.xpath('EXPDATE/text()')[0].extract()
      yield item
