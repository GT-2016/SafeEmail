# coding:utf-8
import os
from SafeEmail.common.base import Base
from SafeEmail.common.device import DeviceConfig
from time import sleep
from appium import webdriver
from SafeEmail.page.login import Login
from SafeEmail.page.sendEmail import SendEmail
if __name__ == "__main__":
    caps = DeviceConfig()
    driver = webdriver.Remote("http://localhost:4723/wd/hub",caps.device_caps)

    se = SendEmail(driver)
    se.click_email_btn()
    se.find_boxs()