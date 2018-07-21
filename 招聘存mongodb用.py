# coding=utf-8
#其实这个网站没必要用selenium，为了练手，用了selenium，多线程，下拉条，存mongodb或者存txt

from selenium import  webdriver
import time
import pymongo
# 多进程
from multiprocessing import Pool

# 1 打开数据库连接，mongodb默认端口为27017
conn = pymongo.MongoClient(host='localhost',port=27017)
# 2 选择或创建数据库
jobdata = conn['baidujobs']
# 3 选择或创建数据集合
ver_job = jobdata['verjob']

baidu_baseurl = 'http://zhaopin.baidu.com/quanzhi?tid=4139&ie=utf8&oe=utf8&query=python%E6%9D%AD%E5%B7%9E&city_sug=%E6%9D%AD%E5%B7%9E'
#下拉条
def set_winscroll(driver):
    time.sleep(2)
    driver.execute_script('window.scrollBy(0,2000)')
    time.sleep(3)
    driver.execute_script('window.scrollBy(0,3000)')
    time.sleep(3)

# 1 初始化driver
driver = webdriver.PhantomJS()
# 2 调用get方法
driver.get(baidu_baseurl)
# 3 进入网页
set_winscroll(driver)

# 4 获取资源（第一页的数据）
we_data = driver.page_source
# print('first_we_data ' + we_data)




def get_content_list(self):
    a=self.driver.find_element_by_xpath("//*[@id='container']/div[2]/div[2]/ul/li[1]")
    a.click()
    self.driver.execute_script('window.scrollBy(0,10000)')
    time.sleep(3)#这个决定下拉条有没有加载完页面

    li_list = self.driver.find_elements_by_xpath("//*[@id='container']/div[3]/div[1]/article/a")
    li_list_href=[li.get_attribute("href") for li in li_list]#列表推倒式获取url然后get进入
    for href in li_list_href:
        self.driver.get(href)
        time.sleep(2)
    #获取详情页信息
        item={}
        item["title"]=self.driver.find_element_by_xpath("//div[@class='head']/h1").text#完全按照一个新网页的xpath来写，是个坑
        # item["file"] = html.xpath("//*[@id='article-DMTP28DM0001899N']/div[2]/div/p").text
        # item["img"] = html.xpath("//*[@id='article-DMTP28DM0001899N']/div[2]/div/div/a/img").get_attribute("src")

        print(item)




def save_content_list(self,content_list):
    pass





if __name__ == '__main__':
    zhaopingSpider()
