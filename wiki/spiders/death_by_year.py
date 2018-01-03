# -*- coding: utf-8 -*-
import scrapy

class DeathByYearSpider(scrapy.Spider):
    name = 'death_by_year'
    
    allowed_domains = ['en.wikipedia.org']
    start_urls = [
        'https://en.wikipedia.org/wiki/Lists_of_deaths_by_year'
        ]
    custom_settings = {
        "DOWNLOAD_DELAY": 0.1,
        "DEPTH_LIMIT"   : 0,     # 0 for no limit
    }
    def start_requests(self):
        cookies={}
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, cookies=cookies)
    def parse(self, response):
        items = response.xpath(u'//tr/td/div/ul/li/a/@href')
        for item in items:
            if item is not None:
                yield response.follow(item, callback=self.parse_detail)
    # TODOs in visited content page.
    def parse_detail(self, response):
        items = response.xpath(
            u'//div[@class="mw-parser-output"]/ul/li/a[1]/following-sibling::text()[1][normalize-space(.)]'
            )
        year = response.url.split('/')[-1]
        # self.logger.info("Target %s ..." % year)
        yield {
          'year': year,
          'sample': items.extract()
        }