# coding:utf-8
"""
Created at 2018.06.21
for log output
@author : Administrator
"""
import logging,time,os
from logging.handlers import RotatingFileHandler

class Logger(object):
    """
    output log
    """
    def __init__(self, title_name):
        title = "logger for safeEmail Project"
        day = time.strftime("%Y%m%d%H", time.localtime(time.time()))
        filepath = os.getcwd()
        files = os.path.join(filepath, day+'.log')
        self.formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logger = logging.Logger(title_name)  # title
        # 不限制文件保存
        self.logfile = logging.FileHandler(files)
        self.logfile.setLevel(logging.DEBUG)        # set log level
        self.logfile.setFormatter(self.formater)
        self.logger.addHandler(self.logfile)
        # control输出到屏幕
        # self.control = logging.StreamHandler()
        # self.control.setLevel(logging.INFO)
        # self.control.setFormatter(self.formater)
        # self.logger.addHandler(self.control)
        # 定义一个RotatingFileHandler，最多备份3个日志文件，每个日志文件最大1K
        # self.rHandler = RotatingFileHandler(file,maxBytes = 512*1024,backupCount = 3)
        # self.rHandler.setLevel(logging.INFO)
        # self.rHandler.setFormatter(self.formater)
        # self.logger.addHandler(self.rHandler)

    def debug_log(self, msg):
        self.logger.debug(msg)

    def info_log(self, msg):
        self.logger.info(msg)

    def warn_log(self, msg):
        self.logger.warning(msg)

    def error_log(self, msg):
        self.logger.error(msg)
if __name__ == "__main__":
    day = time.strftime("%Y%m%d%H", time.localtime(time.time()))
    filepath = os.getcwd()
    file = os.path.join(filepath, day + '.log')
    print(file)