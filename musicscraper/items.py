# -*- coding: utf-8 -*-


import scrapy


class MusicscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title =  scrapy.Field()
    description = scrapy.Field()
    link = scrapy.Field()
    pass
