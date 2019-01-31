# coding=utf-8

from appium import webdriver
import time

desired_caps = {}
desired_caps['deviceName'] = 'DLQ0216406000828'
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
desired_caps['appPackage'] = 'com.waka'
desired_caps['appActivity'] = 'com.waka.mvvm.login.NewLoginActivity'
desired_caps['automationName'] = 'uiautomator2'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
# desired_caps['noReset'] = True
driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
time.sleep(2)

driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
time.sleep(2)

driver.find_element_by_id('com.waka:id/edt_login_email').send_keys(u'quanquandequan@126.com')
driver.find_element_by_id('com.waka:id/edt_login_password').send_keys('123456')
driver.find_element_by_id('com.waka:id/btn_login').click()
driver.swipe()
time.sleep(5)


driver.quit()