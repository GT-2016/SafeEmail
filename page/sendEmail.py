# coding:utf-8
"""
Created at 2018.06.21
function: send emails
"""
import os,time
from SafeEmail.page.login import Login
from SafeEmail.common.base import Base
from SafeEmail.conf.element import Email
from SafeEmail.conf.element import LoginEle
from SafeEmail.log.log import Logger
class SendEmail(Base,Email):
    """firstly to login"""
    log = Logger(os.path.basename(__file__))
    # 如果已经登录可以不用登录
    log.debug_log("login first")

    def click_email_btn(self):
        self.log.debug_log("click email button")
        self.click(self.email_btn)  # 先点击邮件按钮，进入邮件栏

    def find_boxs(self):
        eles = self.findElements(self.emailBox)      # 查找所有的..箱
        return eles

    def is_accounts(self):
        """have how many accounts"""
        # True: many_accounts
        # False: signal accounts
        try:
            self.findElement(self.many_accountName)
            print("many accounts")
            return True
        except Exception as e:
            print("signal account:",e)
            return False

    # ======查找各个邮箱的方法 ================#
    def click_reciveBox(self):
        "click 收件箱"
        flag = self.is_accounts()
        self.click_email_btn()
        ele = self.many_allReciveBox if flag else self.signal_reciveBox
        self.click(ele)

    def click_encryMsgBox(self):
        "click 加密邮箱"
        flag = self.is_accounts()
        self.click_email_btn()
        ele = self.many_allEncryMsgBox if flag else self.signal_encryMsgBox
        self.click(ele)

    def click_starBox(self):
        "click 星标邮箱"
        flag = self.is_accounts()
        self.click_email_btn()
        ele = self.many_allStarBox if flag else self.signal_starBox
        self.click(ele)
    def click_some_account_reciveBox(self, name):
        # argument: email account's name
        self.click_email_btn()
        self.click(("name",name))

    def click_some_account(self, name):
        # 有问题，暂时定位不到账户的名称
        # self.click_email_btn()
        eles = self.findElements(("name",name))
        # print(eles)
        # print(len(eles))

    def input_send_to(self, sendTo):
        """input recived accounts
        输入值规范：send_to = ["liq01@qtec.cn","liq02@qtec.cn","liq03@qtec.cn"]
        """
        send_people = ";".join(sendTo)
        self.sendKeys(self.send_to, send_people)
        # 想发送抄送和密送需要使元素可见
        self.click(self.send_from)
        # self.driver.tap([(700, 620),], 500)
        # self.sendKeys(self.send_cc, send_people)

    def input_subject(self, text):
        "input email sbuject"
        self.sendKeys(self.send_subject, text)

    def input_body(self,content):
        "input email message"
        self.sendKeys(self.send_body, content)

    def input_attach(self):
        "attack: 选不成功"
        # self.sendKeys(self.send_attach, "..//img//Koala.jpg")
        # self.click(self.send_attach)
        self.driver.tap([(936,66),(1080,210)],500)
        self.click(self.send_attach_icon)
        time.sleep(1)
        self.driver.tap([(48,860),(288,1100)],500)

    def send_email(self, sendTo, text, content):
        """
        from many palces to send emails
        :return:
        """
        self.click(self.email_send_btn)
        self.log.debug_log("1. input sendTo")
        self.input_send_to(sendTo)
        self.log.debug_log("2. input email sbuject")
        self.input_subject(text)
        self.log.debug_log("3. input email body")
        self.input_body(content)
        self.log.debug_log("4. send attachment")
        # self.input_attach()
        # self.logout()
        self.click(self.send_btn)
