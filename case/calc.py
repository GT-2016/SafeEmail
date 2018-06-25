# coding:utf-8
from appium import webdriver
import unittest
from time import sleep

from appium.webdriver.common.touch_action import TouchAction

class TestCalc(unittest.TestCase):
    "test calculator2 app"
    def setUp(self):
        """start job"""
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "5.0",
            "deviceName": "emulator-5554",      # 魅族Me2：741AECQL27AL2，m1 note:71MBBKT22P94,calc:emulator-5554
            "appPackage": "com.android.calculator2",
            "appActivity": ".Calculator",
            "automationName": "uiautomator2"
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        sleep(3)
    def test_add(self):
        self.driver.find_element("id", "com.android.calculator2:id/digit_6").click()
        sleep(1)
        self.driver.find_element("id","com.android.calculator2:id/op_add").click()
        sleep(1)
        self.driver.find_element("id", "com.android.calculator2:id/digit_8").click()
        sleep(1)
        result = self.driver.find_element("id","com.android.calculator2:id/result").text
        self.assertEqual('14', result)

    def tearDown(self):
        """after job"""
        TouchAction(self.driver).long_press(self.driver.find_element("id","com.android.calculator2:id/del"))\
        .wait(1000).perform()

if __name__ == "__main__":
    unittest.main()



