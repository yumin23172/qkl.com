# -*- coding: utf-8 -*-
#网页ajax生成，数据更新特别快
import json

import scrapy


class QukuailianSpider(scrapy.Spider):
    name = 'qukuailian'
    allowed_domains = ['okb.com']
    start_urls = ['https://www.okb.com']

    def parse(self, response):
        item={}
        item["href"]="https://www.okb.com/v2/futures/pc/market/marketOverview.do?symbol=f_usd_all"
        print(item)
        yield scrapy.Request(
            item["href"],
            callback=self.parse_heyue,
            meta={"item": item}
        )
    def parse_heyue(self, response):
        item = response.meta["item"]
        alist = []
        y_list=json.loads(response.body.decode())["ticker"]
        # print(y_list)
        for i in y_list:
            item={}
            item["最新价"]=i["buy"]
            item["最高价"] = i["high"]
            alist.append(item)
            print(alist)
           

