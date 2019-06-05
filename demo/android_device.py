# coding=utf-8

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import os

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
sleep(2)

driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
sleep(2)

driver.find_element_by_id('com.waka:id/edt_login_email').send_keys('quanquan@126.com')
driver.find_element_by_id('com.waka:id/edt_login_password').send_keys('666666')
driver.find_element_by_id('com.waka:id/btn_login').click()
sleep(2)

driver.find_element_by_xpath("//*[@text='房屋']").click()
sleep(3)
driver.find_element_by_xpath("//*[@text='继续编辑']").click()
sleep(3)
driver.find_element_by_xpath("//*[@text='关于房屋']").click()
sleep(3)
driver.find_element_by_xpath("//*[@text='下一步']").click()
sleep(3)

def backpage(name):
    """
        返回到指定页面
    """

    i = 0
    while i < 10:
        try:
            findname = "//*[@text='%s']" % (name)
            WebDriverWait(driver, 2).until(
                lambda driver: driver.find_element_by_xpath(findname).is_displayed())
            element = driver.find_element_by_xpath(findname)
            element.click()
            break
        except:
            os.popen("adb shell input keyevent 4")
            # try:
            #     findname = "//*[@text='首页']"
            #     driver.find_element_by_xpath(findname).click()
            #     driver.implicitly_wait(2)
            # except:
            #     os.popen("adb shell input keyevent 4")


backpage('首页')


driver.quit()
