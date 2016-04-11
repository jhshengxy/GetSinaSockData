# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NjuptItem(scrapy.Item):
    news_title = scrapy.Field()
    news_date = scrapy.Field()
    news_url = scrapy.Field()