# coding=utf-8

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep

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
driver.find_element_by_xpath("//*[@text='民居']").click()
sleep(3)
# driver.find_element_by_xpath('//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]').click()
# sleep(3)
# driver.find_element_by_xpath("//*[@text='无标签']").click()
# sleep(3)


element = driver.find_element_by_id('com.waka:id/optionspicker')

element_x = element.size['width']  #element_x为picker的宽，element_y为picker的高
element_y = element.size['height']

start_x = element.location['x'] #start_x，start_y 为picker左上角坐标的x, y
start_y = element.location['y']

begin_x = start_x + element_x / 2
begin_y = start_y + element_y * 5 / 8

end_x = start_x + element_x / 2
end_y = start_y + element_y * 3 / 8

# action.press(x=545, y=1650,).wait(100).move_to(x=545, y=1625).release().perform()
# driver.swipe(545, 1665, 545, 1765, duration=sleep(1))
driver.swipe(begin_x, begin_y, end_x, end_y, duration=sleep(1))
# action.press(x=end_x, y=end_y).wait(100).move_to(x=begin_x, y=begin_y).release().perform()
sleep(3)
driver.quit()
#x=end_x, y=end_y