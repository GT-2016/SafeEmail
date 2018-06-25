# coding:utf-8
"""
Created on 2018.6.20
@author: Administrator
"""
import os,sys
import re,json
from SafeEmail.log.log import Logger
logs = Logger(os.path.basename(__file__))

class DeviceConfig():
    """about devices configure"""
    def __init__(self):
        """
        Constructor
        """
        self.device_caps = {}
        self.device_caps["platformName"] = "Android"
        self.device_caps["platformVersion"] = "5.0.1"
        self.device_caps["deviceName"] = self.getDeviceName()[0]
        self.device_caps["appPackage"] = "com.qtec.safemail2"
        self.device_caps["appActivity"] = ".ui.activities.LaunchActivity"
        self.device_caps["unicodeKeyboard"] = True
        self.device_caps["resetKeyboard"] = True
        self.device_caps["automationName"] = "uiautomator2"

    def getDeviceName(self):
        cmd = "adb devices"
        device_id = []
        try:
            deviceId = os.popen(cmd)
        except Exception as e:
            print("adb devices failed", e)

        for line in deviceId:
            if re.search(r"device$",line):
                ls = line.split("\t")
                device_id.append(ls[0])

        logs.debug_log("devices is %s" % device_id)
        return device_id

    def getJsonDeviceCaps(self):
        """type from dict to json"""
        return json.dumps(self.device_caps)

    def getParentPath(self):
        """get parent path"""
        return os.path.dirname(os.path.dirname(__file__))

    def getAPK(self):
        path = self.getParentPath()
        newpath = os.path.join(path, 'app')
        for app in os.listdir(newpath):
            if re.search(r"apk$",app):
                return os.path.join(newpath,app)

    def installApp(self):
        # "install app package"       # if path is too long, adb command will be failed!!
        logs.debug_log("install QtecSafeMail.apk package")
        apk_path = self.getAPK()
        print(apk_path)
        os.popen("adb install %s"%apk_path)

    def uninstApp(self):
        "uninstall app package"
        logs.debug_log("uninstall QtecSafeMail.apk package")
        os.popen("adb uninstall %s"%self.device_caps["appPackage"])

if __name__ == "__main__":
    d = DeviceConfig()
    d.installApp()
