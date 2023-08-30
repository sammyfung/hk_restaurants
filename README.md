[![codecov](https://codecov.io/gh/sammyfung/HK_Lic_Restaurants/graph/badge.svg?token=RAN18BUKD6)](https://codecov.io/gh/sammyfung/HK_Lic_Restaurants)

Hong Kong Licensed Restaurants Web Scraper
==========================================

Hong Kong Restaurants are licensed by Food and Environmental Hygiene Department in Hong Kong. The department releases an [open data dataset](https://data.gov.hk/en-data/dataset/hk-fehd-fehdlmis-restaurant-licences) of licensees in XML format.

This project uses Scrapy in Python.

Installation
------------

```
$ git clone git@github.com:sammyfung/HK_Lic_Restaurants.git
$ cd HK_Lic_Restaurants
$ python3 -m venv venv
$ source venv/bin/activate  
$ pip install -r requirements.txt
```

Quickstart
----------

Run the web scraper and export scraped data to CSV file.
```
$ cd HK_Lic_Restaurants/HK_Lic_Restaurants    
$ scrapy crawl hkrestaurants -o restaurant_licenses.csv    
```
