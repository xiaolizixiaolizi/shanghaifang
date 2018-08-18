# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewHouseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    province = scrapy.Field()
    city = scrapy.Field()
    name = scrapy.Field()
    rooms = scrapy.Field()
    area = scrapy.Field()
    district = scrapy.Field()
    address = scrapy.Field()
    sale = scrapy.Field()
    desc = scrapy.Field()
    unit_price = scrapy.Field()
    original_url = scrapy.Field()
