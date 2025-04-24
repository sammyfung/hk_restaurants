import scrapy
from hk_restaurants.items import RestaurantItem
import re

class FehdSpider(scrapy.Spider):
    name = "fehd"
    allowed_domains = ["fehd.gov.hk"]
    start_urls = (
        'http://www.fehd.gov.hk/english/licensing/license/text/LP_Restaurants_EN.XML',
        'https://www.fehd.gov.hk/tc_chi/licensing/license/text/LP_Restaurants_TC.XML',
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
        '12': 'Wan Chai',
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
    licenses = {}

    def parse(self, response):
        type_codes = response.xpath('//TYPE_CODE/CODE')
        for type_code in type_codes:
            code = re.sub('#', '', type_code.xpath('@ID').extract()[0])
            description = type_code.xpath('text()').extract()[0]
            self.LICENSE_CODE_TYPE[code] = description

        district_codes = response.xpath('//DIST_CODE/CODE')
        for district_code in district_codes:
            code = re.sub('#', '', district_code.xpath('@ID').extract()[0])
            description = district_code.xpath('text()').extract()[0]
            self.DISTRICT_CODE[code] = description

        info_codes = response.xpath('//INFO_CODE/CODE')
        for info_code in info_codes:
            code = re.sub('#', '', info_code.xpath('@ID').extract()[0])
            description = info_code.xpath('text()').extract()[0]
            self.ADDITION_CODE_TYPE[code] = description

        lics = response.xpath('//LPS/LP')
        for lic in lics:
            license_no = lic.xpath('LICNO/text()')[0].extract()
            license_code = lic.xpath('TYPE/text()')[0].extract()
            license_district_code = lic.xpath('DIST/text()')[0].extract()
            if not self.licenses.get(license_no):
                item = RestaurantItem()
                item['country'] = 'HK'
                item['city'] = 'Hong Kong'
                item['source'] = 'FEHD'
                item['license_no'] = license_no
                item['license_code'] = license_code
                item['license_district_code'] = license_district_code
                item['license_expiry_date'] = lic.xpath('EXPDATE/text()')[0].extract()
                item['name'] = None
                item['address'] = None
                item['chinese_name'] = None
                item['chinese_address'] = None
                item['license_addition_code'] = None
                item['license_addition'] = {}
                self.licenses[license_no] = item

            if re.search('TC.XML', response.url):
                self.licenses[license_no]['license_chinese_type'] = self.LICENSE_CODE_TYPE[license_code]
                self.licenses[license_no]['license_chinese_district'] = self.DISTRICT_CODE[license_district_code]
                self.licenses[license_no]['chinese_name'] = lic.xpath('SS/text()')[0].extract()
                self.licenses[license_no]['chinese_address'] = lic.xpath('ADR/text()')[0].extract()
            else:
                self.licenses[license_no]['license_type'] = self.LICENSE_CODE_TYPE[license_code]
                self.licenses[license_no]['license_district'] = self.DISTRICT_CODE[license_district_code]
                self.licenses[license_no]['name'] = lic.xpath('SS/text()')[0].extract()
                self.licenses[license_no]['address'] = lic.xpath('ADR/text()')[0].extract()

            try:
                if re.search('TC.XML', response.url):
                    if self.licenses[license_no]['license_addition_code'] is None:
                        self.licenses[license_no]['license_addition_code'] = lic.xpath('INFO/text()')[0].extract()
                    self.licenses[license_no]['license_addition']['chinese'] = {}
                    for code in self.licenses[license_no]['license_addition_code'].split('#'):
                        if code != '':
                            self.licenses[license_no]['license_addition']['chinese']['#' + code] = self.ADDITION_CODE_TYPE[code]
                else:
                    if self.licenses[license_no]['license_addition_code'] is None:
                        self.licenses[license_no]['license_addition_code'] = lic.xpath('INFO/text()')[0].extract()
                    self.licenses[license_no]['license_addition']['english'] = {}
                    for code in self.licenses[license_no]['license_addition_code'].split('#'):
                        if code != '':
                            self.licenses[license_no]['license_addition']['english']['#'+code] = self.ADDITION_CODE_TYPE[code]
            except IndexError:
                self.licenses[license_no]['license_addition_code'] = ''

            if self.licenses[license_no]['chinese_name'] is not None and self.licenses[license_no]['name'] is not None:
                yield self.licenses[license_no]
