# coding=utf-8

import unittest
from page.page_login.page_EmailLogin import EmailLogin
from page.page_login.page_Unregistered import Unregistered
from page.page_addHouse.page_AddHotel import AddHotel
from common.getDriver import driver


class LoginTest(unittest.TestCase):
    """登录"""

    def test_01(self):
        """手机账号登录"""
        em = EmailLogin(driver)
        em.operatepe()

    def test_02(self):
        """添加酒店房屋"""
        ho = AddHotel(driver)
        ho.operatepe()

    @unittest.skip("跳过")
    def test_03(self):
        """账号未注册"""
        un = Unregistered(driver)
        un.operatepe()


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(LoginTest('test_01'))
    suite.addTest(LoginTest('test_02'))
    unittest.TextTestRunner(verbosity=2).run(suite)
