# coding:utf-8
"""
Created at 2018.06.21
function: send emails
"""
import os
from SafeEmail.page.login import Login
from SafeEmail.common.base import Base
from SafeEmail.conf.element import Email
from SafeEmail.log.log import Logger
class SendEmail(Base,Email):
    """firstly to login"""
    def __init__(self,driver):
        "login"
        self.log = Logger(os.path.basename(__file__))
        # 如果已经登录可以不用登录
        # log.debug_log("login first")
        # lg = Login(driver)
        # lg.login_email()

    def click_email_btn(self):
        self.log.debug_log("click email button")
        self.click(self.email_btn)  # 先点击邮件按钮，进入邮件栏

    def find_boxs(self):
        eles = self.findElements(self.signal_emailBox)
        print("find eles:",eles)
        print("find eles length:", len(eles))

