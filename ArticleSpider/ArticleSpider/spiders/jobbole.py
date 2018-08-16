# -*- coding: utf-8 -*-
import scrapy
import re

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/114273/'] #['http://blog.jobbole.com/']

    def parse(self, response):
        title = response.xpath("//div[@class='entry-header']/h1/text()").extract()[0]
        time = response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()[0].replace('·', '').strip()
        category = response.xpath("//p[@class='entry-meta-hide-on-mobile']//a/text()").extract()
        # praise = response.xpath("//h10[@id='114273votetotal']/text()").extract()[0]

        praise_nums = response.xpath("//span[contains(@class,'')]/h10/text()").extract()[0]
        fav_nums = response.xpath("//span[contains(@class,'bookmark-btn')]/text()").extract()[0]
        match_re = re.search('.*(\d+).*',fav_nums)
        if match_re:
            fav_nums = match_re.group(1)
        else:
            fav_nums = 0
        comment_nums = response.xpath("//span[contains(@class,'hide-on-480')]/text()").extract()[0]
        match_re = re.search('.*(\d+).*', comment_nums)
        if match_re:
            comment_nums = match_re
        else:
            comment_nums = 0

        content = response.xpath("//div[@id='articleContent']").extract()
        # content = response.xpath("//div[@class='entry']").extract()

        pass
