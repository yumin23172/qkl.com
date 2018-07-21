# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver


class OkbSpider(scrapy.Spider):
    name = 'okb'
    allowed_domains = ['okb.com']
    start_urls = ['https://www.okb.com/marketList']

    # def __init__(self):
    #     super(OkbSpider, self).__init__()
    #     self.driver = webdriver.Chrome()
    #     self.driver.set_page_load_timeout(30)
    # def start_requests(self):
    #     start_urls = ['https://www.okb.com/marketList']
    #     yield scrapy.Request(
    #         'https://www.okb.com/marketList',
    #         callback=self.parse,
    #
    #     )

    def parse(self, response):
        a_list=response.xpath("//tbody//tr")
        print("@"*50)
        print(a_list)
        b_list=[]
        for a in a_list:
            item={}
            item["最新价"] =response.xpath("./td[1]//text()").extract_first()
            item["最高价"] =response.xpath("./td[2]//text()").extract_first()
            b_list.append(item)
            print("$" * 50)
            print(b_list)


    # def closed(self, spider):
    #     print("spider closed")
    #     self.driver.close()