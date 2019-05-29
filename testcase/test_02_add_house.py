# coding=utf-8

import unittest
from page.page_addHouse.page_AddHouseName import AddHouseName
from page.page_addHouse.page_AddHouseCity import AddHouseCity
from page.page_addHouse.page_AddRoom import AddRoom
from page.page_addHouse.page_AddBathroom import AddBathroom
from page.page_addHouse.page_AddKitchen import AddKitchen
from page.page_addHouse.page_AddServices import AddServices
from page.page_addHouse.page_AddRules import AddRules
from page.page_addHouse.page_AddDescriptions import AddDescriptions
from page.page_addHouse.page_AddPictures import AddPictures
from page.page_addHouse.page_AddTag import AddTag
from page.page_addHouse.page_AddCheckinInformation import AddCheckinInformation
from page.page_addHouse.page_AddPrice import AddPrice
from page.page_addHouse.page_AddVerification import AddVerification
from common.getDriver import driver


class AddTest(unittest.TestCase):

#    @unittest.skip("跳过")
    def test_01(self):
        """添加房屋名称"""
        na = AddHouseName(driver)
        na.operatepe()

#    @unittest.skip("跳过")
    def test_02(self):
        """添加房屋位置"""
        ci = AddHouseCity(driver)
        ci.operatepe()

#    @unittest.skip('跳过')
    def test_03(self):
        """添加房型"""
        ro = AddRoom(driver)
        ro.operatepe()

#    @unittest.skip("跳过")
    def test_04(self):
        """添加卫浴设施"""
        ba = AddBathroom(driver)
        ba.operatepe()

#    @unittest.skip("跳过")
    def test_05(self):
        """添加厨房设施"""
        ki = AddKitchen(driver)
        ki.operatepe()

#    @unittest.skip("跳过")
    def test_06(self):
        """添加服务"""
        se = AddServices(driver)
        se.operatepe()

#    @unittest.skip("跳过")
    def test_07(self):
        """添加房屋守则"""
        ru = AddRules(driver)
        ru.operatepe()

#    @unittest.skip("跳过")
    def test_08(self):
        """添加描述信息"""
        de = AddDescriptions(driver)
        de.operatepe()

#    @unittest.skip("跳过")
    def test_09(self):
        """添加图片"""
        pi = AddPictures(driver)
        pi.operatepe()

#    @unittest.skip("跳过")
    def test_10(self):
        """添加图片标签"""
        tag = AddTag(driver)
        tag.operatepe()

#    @unittest.skip("跳过")
    def test_11(self):
        """添加入住信息"""
        checkin = AddCheckinInformation(driver)
        checkin.operatepe()

    def test_12(self):
        """添加价格"""
        price = AddPrice(driver)
        price.operatepe()

    def test_13(self):
        """添加决策人身份验证"""
        ver = AddVerification(driver)
        ver.operatepe()

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(AddTest('test_01'))
    suite.addTest(AddTest('test_02'))
    suite.addTest(AddTest('test_03'))
    suite.addTest(AddTest('test_04'))
    suite.addTest(AddTest('test_05'))
    suite.addTest(AddTest('test_06'))
    suite.addTest(AddTest('test_07'))
    suite.addTest(AddTest('test_08'))
    suite.addTest(AddTest('test_09'))
    suite.addTest(AddTest('test_10'))
    suite.addTest(AddTest('test_11'))
    suite.addTest(AddTest('test_12'))
    suite.addTest(AddTest('test_13'))
    unittest.TextTestRunner(verbosity=13).run(suite)
