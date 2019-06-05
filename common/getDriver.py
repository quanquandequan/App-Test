# coding=utf-8

import time
from appium import webdriver
from selenium.common.exceptions import WebDriverException
from common.ReadConfig import Readconfig
from common.GetDevices import Devices
from common.logs import Log


log = Log()
conf = Readconfig()
cmd = Devices()


class Driver:

    def __init__(self):

        """
            从config配置文件中获取，设备系统：Android，获取App的包名和activity
        """
        self.deviceName = cmd.get_device_name()
        self.platformVersion = cmd.get_platform_version()
        self.platformName = conf.getAppValue('platformName')
        self.appPackage = conf.getAppValue('appPackage')
        self.appActivity = conf.getAppValue('appActivity')

    def get_driver(self):

        desired_caps = {}
        desired_caps['deviceName'] = '%s' % self.deviceName
        desired_caps['platformName'] = '%s' % self.platformName
        desired_caps['platformVersion'] = '%s' % self.platformVersion
        desired_caps['appPackage'] = '%s' % self.appPackage
        desired_caps['appActivity'] = '%s' % self.appActivity
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        # desired_caps['noReset'] = True  #注释之后，每次启动都会自动清除数据
        # desired_caps['newCommandTimeout'] = 180  #超时时间设置为180

        try:
            driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
            time.sleep(5)
            log.info('获取driver成功')
            return driver
        except WebDriverException:
            log.warn('获取driver失败')


if __name__ == '__main__':
    driver = Driver()
    driver.get_driver()
