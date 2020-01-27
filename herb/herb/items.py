# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HerbItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link = scrapy.Field()
    common_name = scrapy.Field()
    origins = scrapy.Field()
    medicinal_uses = scrapy.Field()
    properties = scrapy.Field()
    #family = scrapy.Field()
    description = scrapy.Field()
    #regional_traditions = scrapy.Field()
    folklore = scrapy.Field()
    tags = scrapy.Field()
    #family = scrapy.Field()
    #parts_used = scrapy.Field()

    
