# -*- coding: utf-8 -*-
import scrapy


class LargeheartedboySpider(scrapy.Spider):
    name = "largeheartedboy"
    allowed_domains = ["largeheartedboy.com"]
    start_urls = (
        'http://www.largeheartedboy.com/blog/archive/2014/12/essential_and_i.html',
    )

   eoyl_xpath =' //*[@id="center"]/div/p[6]'
   item_fields = {'title':'.//a/text()',
   'description':'.//text()'
   'link': './/a/@href'}
    def parse(self, response):
        pass
