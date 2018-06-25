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
    qq_company = ('name', 'QQ企业邮箱')                            # 邮箱设置：QQ企业邮箱
    email_139 = ('name', '139邮箱')                            # 邮箱设置：139邮箱
    email_189 = ('name', '189邮箱')                            # 邮箱设置：189邮箱
    imap_finish = ('name', '完成')                             # 邮箱设置：完成
    log_result = ('id', 'com.qtec.safemail2:id/tvTitle')    # 登录结果判断
    setting = ('id', 'com.qtec.safemail2:id/llSettings')    # 设置栏
    email = ("id", "com.qtec.safemail2:id/ivMail")          # 邮件栏按钮
    setting_addAccount = ('name', '添加账户')                   # 添加账户
    setting_oriAccount = ('id', 'com.qtec.safemail2:id/rbOrdinary') # 普通邮箱栏
    setting_back = ('class name', 'android.widget.ImageButton')     # 添加用户返回键
    all_accounts = ("id", "com.qtec.safemail2:id/tvName")           # 所有账户名
    delete_account_btn = ("id", "com.qtec.safemail2:id/tvDeleteAccount")    # 删除账户
    delete_account_confirm = ("id", "com.qtec.safemail2:id/tvPositive")      # 删除账户：确认



class Email():
    """settings elements location"""
    email_send_btn = ("id", "com.qtec.safemail2:id/compose")    # 所有的发送邮件都是一个定位
    email_btn = ("id","com.qtec.safemail2:id/ivMail")           # 邮件栏按钮
    setting_btn = ('id', 'com.qtec.safemail2:id/llSettings')  # 设置栏
    emailBox = ("id", "com.qtec.safemail2:id/tvName")    # 单用户找到了7个元素,多永不不定

    # 单个账户时
    """
    收件箱、密文邮件、星标邮件、草稿箱、已发送、已删除、垃圾箱
    """
    signal_reciveBox = ("name", "收件箱")
    signal_encryMsgBox = ("name", "密文邮件")
    signal_starBox = ("name", "星标邮件")
    signal_draftBox = ("name", "草稿箱")
    signal_haveSentBox = ("name", "已发送")
    signal_havaDelBox = ("name", "已删除")
    signal_dustbinBox = ("name", "垃圾箱")

    # 多账户时
    many_accountName = ("name", "账户")
    many_allReciveBox = ("name", "所有收件箱")
    many_allEncryMsgBox = ("name", "全部密文邮件")
    many_allStarBox = ("name", "全部星标邮件")

    # send emails need
    send_to = ("id", "com.qtec.safemail2:id/to")                    # 收件人
    send_from = ("id", "com.qtec.safemail2:id/fromAddress")        # 发件人
    send_cc = ("id", "com.qtec.safemail2:id/cc")                    # 抄送
    send_bcc = ("id", "com.qtec.safemail2:id/bcc")                  # 密送
    send_subject = ("id", "com.qtec.safemail2:id/etSubject")       # 主题
    send_body = ("id", "com.qtec.safemail2:id/etMessageContent")  # 邮件内容
    send_attach = ("id", "com.qtec.safemail2:id/ivAttachment")     # 附件
    send_attach_icon = ("id", "android:id/icon")
    send_btn = ("id", "com.qtec.safemail2:id/tvRight")             # 发送

    msg_count = ("id", "com.qtec.safemail2:id/tvName")             # 账号邮件入口
    recive_label = ("class name", "android.widget.LinearLayout")  # 统计邮件个数
    all_send_label = ("id", "com.qtec.safemail2:id/list_item_inner")