# coding:utf-8
"""
Created at 2018.06.21
@author : Administrator
"""
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base(object):
    """Base Class"""
    def __init__(self, driver):
        "init config"
        self.driver = driver
        self.timeout = 90
        self.poll = 0.5

    def findElement(self, args):
        """
        args: 传元祖 （'id','xx'）
        """
        #         args:(by, value)
        #         driver.find_element("id", "kw")
        #         driver.find_element("xpath", "//*[@id='kw']")
        #         driver.find_element("css selector", "#kw")
        #         driver.find_element("class name", "xxx")
        #         driver.find_element("tag name","xxxxxx")
        #         """

        # 查找某个元素
        try:
            ele = WebDriverWait(self.driver, self.timeout, self.poll).until(lambda x: x.find_element(*args))
            return ele
        except Exception as e:
            print("Faile to getElement %s"%e)
            return False

    def findElements(self, args):
        # 查找某些元素
        ele = WebDriverWait(self.driver, self.timeout, self.poll).until(lambda x: x.find_elements(*args))
        return ele

    def clickEle(self, args, n=0):
        # 点击 n=?的元素
        ele = self.findElements(args)
        length = len(ele)
        if length < 1:
            print("Don't find the element")
        elif length < n:
            print("out of the max number")
        else:
            ele[n].click()

    def click_n(self,ele,n=0):
        """have found ele"""
        ele[n].click()

    def sendKeys(self, args, text):
        # 向某个找到的元素发送文本
        ele = self.findElement(args)
        ele.send_keys(text)

    def click(self, args):
        # 点击某个找到的元素按钮
        ele = self.findElement(args)
        ele.click()

    def clear(self, args):
        # 清空某个找到元素的文本
        ele = self.findElement(args)
        ele.clear()

    def moveToEle(self, args):
        """
        鼠标悬停事件
        """
        ele = self.findElement(args)
        ActionChains(self.driver).move_to_element(ele).perform()

    def is_alert_exsit(self, timeout=15):
        # 判断alert框是否存在
        alert = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.alert_is_present())
        return alert

    def is_find_element(self, args):
        """whether find that element"""
        try:
            ele = self.findElement(args)
            return True
        except Exception as e:
            return False

    def get_elements_num(self, args):
        try:
            eles = self.findElements(args)
            return len(eles)
        except Exception as e:
            return False

    def get_toast(self, message):
        """find toast by context"""
        toast = ("xpath", ".//[contains(@text,'%s')]"%message)
        try:
            ele = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.presence_of_element_located(toast))
            # ele = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.presence_of_element_located(("link text",message)))
            print("toast found: %s"%ele)
            return ele
        except Exception as e:
            return False

    def getSize(self):
        """get screen width and height"""
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    # 屏幕向上滑动
    def swipeUp(self,t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.75)  # 起始y坐标
        y2 = int(l[1] * 0.25)  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2, t)

    # 屏幕向下滑动
    def swipeDown(self,t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.25)  # 起始y坐标
        y2 = int(l[1] * 0.75)  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2, t)

    # 屏幕向左滑动
    def swipLeft(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.75)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.05)
        self.driver.swipe(x1, y1, x2, y1, t)

    # 屏幕向右滑动
    def swipRight(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.05)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.75)
        self.driver.swipe(x1, y1, x2, y1, t)

    def logout(self):
        "logout"
        self.driver.quit()