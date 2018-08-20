# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MafengwoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collection = 'mafengwo'
    city_area = scrapy.Field()
    article_title = scrapy.Field()
    create_time = scrapy.Field()
    article_path = scrapy.Field()


class MafengwoCityItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collection = 'mafengwo'
    city = scrapy.Field()
    introduction_article = scrapy.Field()

