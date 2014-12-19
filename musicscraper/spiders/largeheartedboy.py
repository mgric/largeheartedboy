# -*- coding: utf-8 -*-
import scrapy
from musicscraper.items import MusicscraperItem

class LargeheartedboySpider(scrapy.Spider):
    name = "largeheartedboy"
    allowed_domains = ["largeheartedboy.com"]
    start_urls = ['http://www.largeheartedboy.com/blog/archive/2014/12/essential_and_i.html']
    
    #item_fields = {'title':'.//a/text()','description':'.//text()','link': './/a/@href'}
    def parse(self, response):
        
    	eoyl_xpath = '//*[@id="center"]/div/p[6]'

    	for eoyl in response.xpath('//*[@id="center"]/div/p/a'):

    		item = MusicscraperItem()
    		item['title'] =eoyl.xpath('text()').extract()
    		item['link'] =eoyl.xpath('@href').extract()
    		#desc = eoyl.xpath('text()')
    		#print "title:", item['title']
    		#print 'link:' , item['link']
    		#print 'description:', desc
    		yield item
        
