# coding:utf-8
"""
Created on 2018.6.21
@author: Administrator
"""
import os
from SafeEmail.common.base import Base
from SafeEmail.common.device import DeviceConfig
from SafeEmail.conf.element import LoginEle
from SafeEmail.log.log import Logger

class Login(Base, LoginEle):
    "login function"

    log = Logger(os.path.basename(__file__))
    loginActivity = ".ui.activities.LoginActivity"     # login page activity

    def input_user_psd(self, user, psd):
        self.log.debug_log("1. input email username")
        self.sendKeys(self.login_user, user)
        self.log.debug_log("2. input email password")
        self.sendKeys(self.login_psd, psd)

    def click_setup_email(self):
        """点击邮箱设置，正常流程"""
        try:
            self.log.debug_log("3. click email server setup")
            self.click(self.setup_email)
            self.log.debug_log("4. click email server QQ company setup")
            self.click(self.qq_com)
            self.log.debug_log("5. click email server setup finished")
            self.click(self.imap_finish)
        except:
            self.log.error_log("click_setup_email False!")

    def login_email(self, user='liq01@qtec.cn', psd='Abc1234'):
        # 第一次登录，必须是加密邮箱
        # 1. 输入邮箱账号和密码
        self.driver.wait_activity(self.loginActivity, 30, 1)
        try:
            self.input_user_psd(user, psd)
            # 2. 完成设置页
            self.click_setup_email()
            # 3. 点击登录按钮
            self.log.debug_log("6. click login button")
            self.click(self.login_btn)
        except:
            self.log.error_log("click login Failed!")
        self.log.debug_log("wait for at least 30 seconds for scan the QK code")
        self.driver.wait_activity(self.loginActivity, 30, 1)

    def add_account(self, args, flag):
        """添加账户，flag=True表示是加密账号，flag=False表示是普通账号"""
        lens = len(args)
        for i in range(lens):
            self.log.debug_log("click setup")
            self.click(self.setting)
            self.log.debug_log("add accounts")
            self.click(self.setting_addAccount)
            if not flag:
                self.log.debug_log("add oridinary accounts")
                self.click(self.setting_oriAccount)
            # 输入用户名、密码(密码是int)
            self.login_email(args[i]["user"], args[i]["psd"])
            ele = self.findElements(self.add_result)
            self.log.debug_log("all accounts %s"%ele)   # 查看全部账号
            #             print self.login_result(self.add_result, args[i]["result"])
            try:
                self.click(self.setting_back)
            except:
                self.log.error_log("setting back failed")


if __name__ == "__main__":
    pass