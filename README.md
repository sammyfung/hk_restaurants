Scraper of Licensed Restaurants in Hong Kong
============================================

Food and Environmental Hygiene Department in Hong Kong Government released an [open data dataset](https://data.gov.hk/en-data/dataset/hk-fehd-fehdlmis-restaurant-licences) (in XML format) contains information of licensed restaurants in Hong Kong. This scraper is written in python, with use of scrapy web scraping framework.

Installation
------------

$ pip install -r requirements.txt
```
$ git clone git@github.com:sammyfung/LP_Restaurants_Scrapy.git
$ cd LP_Restaurants_Scrapy
$ python3 -m venv venv
$ source venv/bin/activate  
$ pip install -r requirements.txt
```

Running
-------

Do the web crawling and export into CSV file.
````
$ cd LP_Restaurants_Scrapy/LP_Restaurants_Scrapy    
$ scrapy crawl rlxml -o restaurant_licenses.csv    
```
