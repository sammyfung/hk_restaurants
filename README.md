[![HK_Lic_Restaurants](https://github.com/sammyfung/hk_restaurants/actions/workflows/python-app.yml/badge.svg)](https://github.com/sammyfung/hk_restaurants/actions/workflows/python-app.yml)
[![codecov](https://codecov.io/gh/sammyfung/hk_restaurants/graph/badge.svg?token=RAN18BUKD6)](https://codecov.io/gh/sammyfung/hk_restaurants)

Hong Kong Restaurants Web Scraper
==========================================

This project is aimed to scrape restaurants information from websites. Currently, fehd ([Licensed Restaurant registered with Food and Environmental Hygiene Department in Hong Kong](https://data.gov.hk/en-data/dataset/hk-fehd-fehdlmis-restaurant-licences))is the only spider available in this project.

Installation
------------

```
$ git clone git@github.com:sammyfung/hk_restaurants.git
$ cd hk_restaurants
$ python3 -m venv venv
$ source venv/bin/activate  
$ pip install -r requirements.txt
```

Quickstart
----------

Run the web scraper and export scraped data to CSV file.
```
$ cd hk_restaurants/hk_restaurants    
$ scrapy crawl fehd -o fehd.csv    
```
