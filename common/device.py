# coding:utf-8
"""
Created on 2018.6.20
@author: Administrator
"""
import os
import re,json
from SafeEmail.log.log import Logger
class DeviceConfig(Logger):
    """about devices configure"""
    def __init__(self):
        """
        Constructor
        """
        self.device_caps = {}
        self.device_caps["platformName"] = "Android"
        self.device_caps["platformVersion"] = "5.1"
        self.device_caps["deviceName"] = self.getDeviceName()[0]
        self.device_caps["appPackage"] = "com.qtec.safemail2"
        self.device_caps["appActivity"] = ".ui.activities.LaunchActivity"
        self.device_caps["unicodeKeyboard"] = True
        self.device_caps["resetKeyboard"] = True

        self.log = Logger(os.path.basename(__file__))

    def getDeviceName(self):
        cmd = "adb devices"
        device_id = []
        try:
            deviceId = os.popen(cmd)
        except Exception as e:
            print("adb devices failed", e)

        for line in deviceId:
            if re.findall(r"device$",line):
                ls = line.split("\t")
                device_id.append(ls[0])
        return device_id

    def getJsonDeviceCaps(self):
        """type from dict to json"""
        return json.dumps(self.device_caps)

    def installApp(self):
        # "install app package"       # if path is too long, adb command will be failed!!
        self.log.debug_log("install QtecSafeMail-0607.apk package")
        path = "D:\\QtecSafeMail-0607.apk"
        os.popen("adb install %s"%path)

    def uninstApp(self):
        "uninstall app package"
        self.log.debug_log("uninstall QtecSafeMail-0607.apk package")
        os.popen("adb uninstall %s"%self.device_caps["appPackage"])
