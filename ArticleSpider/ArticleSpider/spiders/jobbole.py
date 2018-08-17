# -*- coding: utf-8 -*-
import scrapy
import re

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/114273/'] #['http://blog.jobbole.com/']

    def parse(self, response):
        #
        # # 采用xpath方式
        # title = response.xpath("//div[@class='entry-header']/h1/text()").extract()[0]
        # create_time = response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()[0].replace('·', '').strip()
        # tag_list = response.xpath("//p[@class='entry-meta-hide-on-mobile']//a/text()").extract()
        # tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        # # praise = response.xpath("//h10[@id='114273votetotal']/text()").extract()[0]
        #
        # praise_nums = response.xpath("//span[contains(@class,'')]/h10/text()").extract()[0]
        # fav_nums = response.xpath("//span[contains(@class,'bookmark-btn')]/text()").extract()[0]
        # match_re = re.search('.*(\d+).*',fav_nums)
        # if match_re:
        #     fav_nums = match_re.group(1)
        # else:
        #     fav_nums = 0
        # comment_nums = response.xpath("//span[contains(@class,'hide-on-480')]/text()").extract()[0]
        # match_re = re.search('.*(\d+).*', comment_nums)
        # if match_re:
        #     comment_nums = match_re
        # else:
        #     comment_nums = 0
        #
        # content = response.xpath("//div[@id='articleContent']").extract()
        # # content = response.xpath("//div[@class='entry']").extract()

        # 采用Csss 方式
        title = response.css(".entry-header h1::text").extract()
        create_time = response.css(".entry-meta-hide-on-mobile::text").extract()[0].strip().replace('·', '').strip()
        tag_list = response.css(".entry-meta-hide-on-mobile a::text").extract()
        tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        tags = ','.join(tag_list)
        praise_nums = response.css(".btn-bluet-bigger h10::text").extract()[0]
        fav_nums = response.css(".bookmark-btn::text").extract()[0]
        match_re = re.search('.*(\d+).*', fav_nums)
        if match_re:
            fav_nums = match_re.group(1)
        else:
            fav_nums = 0
        comment_nums = response.css("a[href='#article-comment'] span::text").extract()[0]
        match_re = re.search('.*(\d+).*', comment_nums)
        if match_re:
            comment_nums = match_re
        else:
            comment_nums = 0
        content = response.css("div.entry").extract()

        pass
