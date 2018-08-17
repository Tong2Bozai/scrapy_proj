# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
from urllib import parse

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/'] #['http://blog.jobbole.com/']

    def parse(self, response):
        """
        1'获取文章列表页中的文章的url交给解析函数，进行具体内容字段的解析
        2.获取文章列表页的url，交给scrapy下载
        :param response:
        :return:
        """
        #获取文章详情的url
        post_urls = response.css('#archive .floated-thumb .post-thumb a::attr(href)').extract()
        for post_url in post_urls:
            print(post_url)
            yield Request(url=parse.urljoin(response.url,post_url),callback=self.parse_detail)
        next_urls = response.css(".next.page-numbers::attr(href)").extract_first()
        if next_urls:
            yield Request(url=parse.urlparse(response.url,post_url),callback=self.parse)

    def parse_detail(self,response):
        """
        提取文章的具体字段
        采用xpath方式解析
        :param response:
        :return:
        """
        title = response.xpath("//div[@class='entry-header']/h1/text()").extract()[0]
        create_time = response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()[0].replace('·', '').strip()
        tag_list = response.xpath("//p[@class='entry-meta-hide-on-mobile']//a/text()").extract()
        tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
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
        pass
        # content = response.xpath("//div[@class='entry']").extract()

    # # 采用Csss 方式
    # title = response.css(".entry-header h1::text").extract()
    # create_time = response.css(".entry-meta-hide-on-mobile::text").extract()[0].strip().replace('·', '').strip()
    # tag_list = response.css(".entry-meta-hide-on-mobile a::text").extract()
    # tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
    # tags = ','.join(tag_list)
    # praise_nums = response.css(".btn-bluet-bigger h10::text").extract()[0]
    # fav_nums = response.css(".bookmark-btn::text").extract()[0]
    # match_re = re.search('.*(\d+).*', fav_nums)
    # if match_re:
    #     fav_nums = match_re.group(1)
    # else:
    #     fav_nums = 0
    # comment_nums = response.css("a[href='#article-comment'] span::text").extract()[0]
    # match_re = re.search('.*(\d+).*', comment_nums)
    # if match_re:
    #     comment_nums = match_re
    # else:
    #     comment_nums = 0
    # content = response.css("div.entry").extract()

