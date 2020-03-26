# coding=utf-8

from appium import webdriver
import time

desired_caps = {}
desired_caps['deviceName'] = "iPhone 6 Plus"
desired_caps['platformName'] = 'ios'
desired_caps['platformVersion'] = '12.4.5'
desired_caps['bundleId'] = 'tv.douyu.live'     # 包名
desired_caps['udid'] = '3bbbba5b327768ef67c584f5f5ed17e7e1b5c6b0'
desired_caps['AutomationName'] = 'XCUITest'
desired_caps['xcodeOrgId'] = "quanquandequan@126.com"
desired_caps['xcodeSigningId'] = "iPhone Developer"
# desired_caps['no-reset'] = True
# desired_caps['app'] = "/Users/woody/Downloads/TDMainClient-Release.ipa"
driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
time.sleep(2)

