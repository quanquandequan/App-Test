# coding=utf-8

import os
from common.Operate import Operate

PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )
yamlpath = PATH("E:\\App-Test\\testyaml\\AddHouse\\01_AddHouseName.yaml")


class AddHouseName:

    def __init__(self, driver):
        self.path = yamlpath
        self.driver = driver
        self.operate = Operate(self.path, self.driver)

    def operatepe(self):
        self.operate.check_operate_type()
