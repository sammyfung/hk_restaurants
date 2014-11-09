Scraper of Licensed Restaurants in Hong Kong
============================================

Developed by Sammy Fung <sammy@sammy.hk>

Food and Environmental Hygiene Department in Hong Kong Governement released a PSI dataset (in XML format) contains information of licensed restaurants in Hong Kong. This scraper is written in python, with use of scrapy web scraping framework.

Data.One Dataset: http://www.gov.hk/en/theme/psi/datasets/restaurantlicences.htm

Installation
------------

$ pip install -r requirements.txt    
$ git clone https://github.com/sammyfung/LP_Restaurants_Scrapy    
$ cd LP_Restaurants_Scrapy/LP_Restaurants_Scrapy    
$ scrapy crawl rlxml -t json -o -o restaurant_licenses.json    

