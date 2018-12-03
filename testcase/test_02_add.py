# coding=utf-8

import unittest
from page.page_addHouse.page_AddHotel import AddHotel
from common.getDriver import driver


class AddTest(unittest.TestCase):

    def test_01(self):
        """添加酒店房屋"""
        em = AddHotel(driver)
        em.operatepe()


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(AddTest('test_01'))
    unittest.TextTestRunner(verbosity=1).run(suite)
