# -*- coding: utf-8 -*-
#scrapy中用cookie模拟登陆再获取数据，有的登陆后还要验证码的就用打码平台
#selenium就用如方法
import scrapy
import re


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/327550029/profile']

    def start_requests(self):
        cookies = "anonymid=jcokuqturos8ql; depovince=GW; jebecookies=f90c9e96-78d7-4f74-b1c8-b6448492995b|||||; _r01_=1; JSESSIONID=abcx4tkKLbB1-hVwvcyew; ick_login=ff436c18-ec61-4d65-8c56-a7962af397f4; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; p=90dea4bfc79ef80402417810c0de60989; first_login_flag=1; ln_uact=mr_mao_hacker@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn421/20171230/1635/main_JQzq_ae7b0000a8791986.jpg; t=24ee96e2e2301bf2c350d7102956540a9; societyguester=24ee96e2e2301bf2c350d7102956540a9; id=327550029; xnsid=e7f66e0b; loginfrom=syshome; ch_id=10016"
        cookies = {i.split("=")[0]:i.split("=")[1] for i in cookies.split("; ")}
        # headers = {"Cookie":cookies}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
            # headers = headers
        )

    def parse(self, response):
        print(re.findall("毛兆军",response.body.decode()))
        yield scrapy.Request(
            "http://www.renren.com/327550029/profile?v=info_timeline",
            callback=self.parse_detial
        )

    def parse_detial(self,response):
        print(re.findall("毛兆军",response.body.decode()))


#selenim方法登陆微博：
from selenium import webdriver
import time
start_url = "http://3g.163.com/touch/news/"
driver = webdriver.PhantomJS()
driver.get(start_url)
time.sleep(5)

a = driver.find_element_by_xpath('//*[@id="loginname"]')
a.send_keys('微博账号')

# 密码
b = driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input')
b.send_keys('微博密码')

time.sleep(3)
# 登录按钮
c = driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a')
c.click()