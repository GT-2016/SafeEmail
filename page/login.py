# coding:utf-8
"""
Created on 2018.6.21
@author: Administrator
"""
import os,time
from SafeEmail.common.base import Base
from SafeEmail.common.device import DeviceConfig
from SafeEmail.data.element import LoginEle
from SafeEmail.log.log import Logger

class Login(Base, LoginEle):
    "login function"

    log = Logger(os.path.basename(__file__))
    loginActivity = ".ui.activities.LoginActivity"     # login page activity

    def swipLeft4(self):
        for i in range(4):
            print("left swip %d"%i)
            self.swipLeft(500)
        time.sleep(15)

    def input_user_psd(self, user, psd):
        self.log.debug_log("1. input email username")
        self.sendKeys(self.login_user, user)
        self.log.debug_log("2. input email password")
        self.sendKeys(self.login_psd, psd)

    def click_setup_email(self, type):
        """点击邮箱设置，正常流程"""
        # type: 1 means QQ mailbox
        # type: 2 means QQ company mailbox  # default qq_company
        # type: 3 means 139 mailbox
        # type: 4 means 189 mailbox
        try:
            self.log.debug_log("3. click email server setup")
            self.click(self.setup_email)
            self.log.debug_log("4. click email server mailbox type %d"%type)
            if type == 1:
                self.click(self.qq_email)
            elif type == 3:
                self.click(self.email_139)
            elif type == 4:
                self.click(self.email_189)
            else:
                self.click(self.qq_company)

            self.log.debug_log("5. click email server setup finished")
            self.click(self.imap_finish)
        except:
            self.log.error_log("click_setup_email False!")

    def login_email(self, user='liq01@qtec.cn', psd='Abc12345',type=2):
        # 第一次登录，必须是加密邮箱
        # 1. 输入邮箱账号和密码
        self.driver.wait_activity(self.loginActivity, 30, 1)
        print("1.....")
        try:
            self.input_user_psd(user, psd)
            print("2.....")
            # 2. 完成设置页
            # self.click_setup_email(type)
            print("3.....")
            # 3. 点击登录按钮
            self.log.debug_log("6. click login button")
            # print("4.....")
            time.sleep(20)
            self.click(self.login_btn)
        except:
            self.log.error_log("click login Failed!")
        self.log.debug_log("wait for at least 30 seconds for scan the QK code")

        ele = self.get_toast("网络不可用,请检查网络状态")
        print("toast",ele)

    def login_result(self, res):
        ele = self.get_toast(res)
        if ele:
            self.log.error_log("toast: 登录错误判断")
        else:
            return True

    def add_account(self, arr, entry="setting" ,flag=True):
        """添加账户，flag=True表示是加密账号，flag=False表示是普通账号"""
        # arr=[()],default entry means from settings to add account
        for i in arr:
            self.log.debug_log("from %s to add accounts"%entry)
            if entry == 'email' and self.is_accounts():
                self.click(self.email)
            else:
                self.click(self.setting)

            self.log.debug_log("add accounts")
            self.click(self.setting_addAccount)
            if not flag:
                self.log.debug_log("add oridinary accounts")
                self.click(self.setting_oriAccount)
            # 输入用户名、密码(密码是int)
            self.login_email(i[0], i[1])
            ele = self.add_account_result()
            ele and self.log.debug_log("all accounts %s"%len(ele))   # 从设置栏处查看全部账号
            ele and self.log.debug_log("add after: %s"%ele[1].text)    # 添加的账户名称
            not ele and self.log.error_log("add account Failed!!")
            # try:
            #     self.click(self.setting_back)
            # except:
            #     self.log.error_log("setting back failed")

    def add_account_result(self):
        try:
            self.click(self.setting)
            ele = self.findElements(self.all_accounts)
            return ele
        except Exception as e:
            self.log.debug_log("time out !! not found add account result")
            return False

    def delete_account(self, n=-1):
        """delete account: default delete the last one"""
        self.click(self.setting)
        eles = self.findElements(self.all_accounts)
        before_num = len(eles)
        if n > before_num-1:
            n = before_num -1
        self.click_n(eles, n)
        self.click(self.delete_account_btn)
        self.click(self.delete_account_confirm)
        after_eles = self.findElements(self.all_accounts)
        after_num = len(after_eles)
        if before_num - after_num == 1:
            print("delete success!!")
            self.log.debug_log("delete %s success!!"%eles[n])

    def is_accounts(self):
        """have how many accounts"""
        # True: many_accounts
        # False: signal accounts
        eles = self.findElements(self.setting_btn)
        if len(eles) > 1:
            print("total %d accounts"%len(eles))
            return True
        else:
            print("signal account")
            return False

if __name__ == "__main__":
    pass