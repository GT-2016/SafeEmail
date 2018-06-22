# coding:utf-8
"""
Created at 2018.06.21
@author : Administrator
"""
class LoginEle():

    login_user = ('id', 'com.qtec.safemail2:id/etUser') # 邮箱用户名
    login_psd = ('id', 'com.qtec.safemail2:id/etPwd')   # 邮箱密码
    login_btn = ('id', 'com.qtec.safemail2:id/btnLogin')    # 邮箱登录按钮
    setup_email = ('id', 'com.qtec.safemail2:id/tvSetting') # 邮箱设置
    qq_email = ('name', 'QQ邮箱')                              # 邮箱设置：QQ邮箱
    qq_com = ('name', 'QQ企业邮箱')                            # 邮箱设置：QQ企业邮箱
    email_139 = ('name', '139邮箱')                            # 邮箱设置：139邮箱
    email_189 = ('name', '189邮箱')                            # 邮箱设置：189邮箱
    imap_finish = ('name', '完成')                             # 邮箱设置：完成
    log_result = ('id', 'com.qtec.safemail2:id/tvTitle')    # 登录结果判断
    setting = ('id', 'com.qtec.safemail2:id/llSettings')    # 设置栏
    setting_addAccount = ('name', '添加账户')
    setting_oriAccount = ('id', 'com.qtec.safemail2:id/rbOrdinary')
    setting_back = ('class name', 'android.widget.ImageButton')

    email = ('id', 'com.qtec.safemail2:id/ivMail')
    send_email = ('id', 'com.qtec.safemail2:id/compose')
    send_to = ('id', 'com.qtec.safemail2:id/to')  # 收件人
    send_subject = ('id', 'com.qtec.safemail2:id/etSubject')  # 主题
    send_body = ('id', 'com.qtec.safemail2:id/etMessageContent')  # 邮件内容
    send_btn = ('id', 'com.qtec.safemail2:id/tvRight')
    msg_count = ('id', 'com.qtec.safemail2:id/tvName')  # 账号邮件入口
    recive_label = ('class name', 'android.widget.LinearLayout')  # 统计邮件个数
    all_send_label = ('id', 'com.qtec.safemail2:id/list_item_inner')

class Email():
    """settings elements location"""
    email_send_btn = ("id", "com.qtec.safemail2:id/compose")    # 所有的发送邮件都是一个定位
    email_btn = ("id","com.qtec.safemail2:id/ivMail")
    # 单个账户时

    signal_emailBox = ("id", "com.qtec.safemail2:id/tvName")
