from selenium import webdriver
import time
import selenium

class WangyiyunSpider:
    def __init__(self):
        self.start_url = "https://music.163.com/#/discover/playlist/"
        self.driver = webdriver.PhantomJs()

    def get_content_list(self):
        self.driver.switch_to.frame("g_iframe")
        y=self.driver.find_element_by_id("cateToggleLink")
        y.click()
        time.sleep()
        # self.driver.switch_to.frame("xh-bar")
        # div = self.driver.find_element_by_id('cateListBox')

        li_list = self.driver.find_elements_by_class_name("s-fc1 ")
        li_list_href = [list.get_attribute("href") for list in li_list]
        print(li_list_href)
        for yy in li_list_href:
            self.driver.get(yy)
            self.driver.switch_to.frame("g_iframe")
            time.sleep(2)
            y_list=self.driver.find_elements_by_xpath("//p[@class='dec']/a")
            y_list_href=[href.get_attribute("href") for href in y_list]
            print(y_list)
            content_list = []
            for mm in y_list_href:
                self.driver.get(mm)
                self.driver.switch_to.frame("g_iframe")
                time.sleep(2)
                item = {}
                item["wyy_name"] = self.driver.find_element_by_xpath(".//a[@class='s-fc7']").text
                # item["wyy_name"] = self.driver.find_element_by_xpath(".//div[@class='tit']/h2").text
                print(item)
                content_list.append(item)
            next_url = self.driver.find_elements_by_xpath(".//a[@class='zbtn znxt']")
            next_url=next_url[0] if len(next_url)>0 else None
            return content_list, next_url






        # next_url = self.driver.find_elements_by_xpath(".//a[@class='zbtn znxt']")
        # next_url=next_url[0] if len(next_url)>0 else None
        # return content_list, next_url

    def save_content_list(self,content_list):
        pass

    def run(self):
        # 1.start_url
        # 2.发请求,获取响应
        self.driver.get(self.start_url)
        # 3.提取数据,,获取下一页url地址
        content_list, next_url = self.get_content_list()
        # 3.保存
        self.save_content_list(content_list)
        # 4 .请求下一页url,循环
        while next_url is not None:
            next_url.click()
            time.sleep(10)
            content_list, next_url = self.get_content_list()
            self.save_content_list(content_list)


if __name__ == '__main__':
    wyy = WangyiyunSpider()
    wyy.run()
