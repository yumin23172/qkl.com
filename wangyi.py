# coding=utf-8
#网易新闻的登陆，网站ajax生成，每页都有下拉条也是ajax生成
from selenium import  webdriver
import time



class wangyiSpider:
    def __init__(self):
        self.start_url = "http://3g.163.com/touch/news/"
        self.driver = webdriver.Chrome()


    def get_content_list(self):
        a=self.driver.find_element_by_xpath("//*[@id='container']/div[2]/div[2]/ul/li[1]")
        a.click()
        #  让页面滚动到下面
        self.driver.execute_script("window.scrollBy(0,3000)")
        time.sleep(3)

        self.driver.execute_script("window.scrollBy(0,5000)")
        time.sleep(3)
        # self.driver.execute_script('window.scrollBy(0,10000)')
        # time.sleep(3)#这个决定下拉条有没有加载完页面

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


    def run(self):#实现主要逻辑
        #1.start_url
        #2.发送请求，获取响应
        self.driver.get(self.start_url)
        #3.提取数据，提取下一页的元素
        content_list = self.get_content_list()
        #4.保存数据
        self.save_content_list(content_list)



if __name__ == '__main__':
    wy= wangyiSpider()
    wy.run()