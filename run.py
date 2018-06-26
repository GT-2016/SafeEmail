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
    # driver.tap(['520','123'],30)
    # driver.swipe(start_x=0,start_y=1700,end_x=0,end_y=200)
    # 登录
    lg = Login(driver)
    sleep(15)
    lg.swipLeft4()
    lg.login_email()

#     se = SendEmail(driver)
#     send_to = ["liq01@qtec.cn","liq02@qtec.cn","liq03@qtec.cn"]
#     subject = "发送测试邮件！！"
#     content = " 湛湛长空黑。更那堪、斜风细雨，乱愁如织。老眼平生空四海，赖有高楼百尺。看浩荡、千崖秋色。白发书生神州泪，尽凄凉、不向牛山滴。追往事，去无迹。\
# 少年自负凌云笔。到而今、春华落尽，满怀萧瑟。常恨世人新意少，爱说南朝狂客。把破帽、年年拈出。若对黄花孤负酒，怕黄花、也笑人岑寂。鸿北去，日西匿。\
#               "
#     se.send_email(send_to, subject, content)

    # lg = Login(driver)
    # account = [("liq04@qtec.cn","Abc1234"),("liq05@qtec.cn","Abc1234")]
    # lg.add_account(account)
    # lg.delete_account(-1)
