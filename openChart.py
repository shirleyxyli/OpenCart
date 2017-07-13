# -*- coding:UTF-8 -*-
from selenium import webdriver
import selenium.webdriver.remote.webdriver
import time
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# 打开浏览器
def browser(browser):
    try:
        if browser == 'ff':
            driver = webdriver.Firefox()
            return driver
        elif browser == 'ch':
            driver = webdriver.Chrome()
            return driver
        elif browser == 'ie':
            driver = webdriver.Ie()
            return driver
        elif browser == 'pj':
            driver = webdriver.PhantomJS()
            return driver
        else:
            print("驱动失败")
    except Exception as msg:
        print("%s" % msg)


# 点击动作click
def click(self, locator):
    element = self.find_element(locator)
    element.click()


# 显示等待找元素
def find_element(self, locator, timeout=10):
    element = WebDriverWait(self, timeout, 1).until(EC.presence_of_element_located(locator))
    return element


def saveTxt(filename, text):
    mdir = sys.path[0] + '\\'
    with open(mdir + filename, "r", encoding="UTF-8") as ifile:
        ifile.write(text)


if __name__ == "__main__":
    # 启动浏览器
    #d = browser('ff')
    d = driver = selenium.webdriver.remote.webdriver.WebDriver('http://localhost:4445/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX)
    times = 5
    d.get("https://gbeta10.banggood.com")
    time.sleep(2)
    chart = d.find_element_by_id("cart_nums_id")
    chart.click()
    """ 首页点击购物车
    for i in range(0,times):
        d.get("https://gbeta10.banggood.com")
        time.sleep(2)
        chart = d.find_element_by_id("cart_nums_id")
        chart.click()
        time.sleep(2)
        d.delete_all_cookies()
   """
    for i in range(0, times):
        d.refresh()
        uid = d.get_cookie("rec_uid")['value']
        sid = d.get_cookie("rec_sid")['value']
        u = uid.find("|")
        s = sid.find("|")
        print("rec_uid: " + uid[0:u - 1])
        print("rec_sid: " + sid[0:s - 1])
        #saveTxt("text.txt", "rec_uid: " + uid[0:u - 1] + ',' + "rec_sid: " + sid[0:s - 1])
        time.sleep(1)
        d.delete_all_cookies()
        d.refresh()
    # 关闭浏览器
    d.quit()
