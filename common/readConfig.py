# coding=utf-8

import os
import configparser

prjDir = os.path.split(os.path.realpath(__file__))[0]
configfile_path = os.path.join(prjDir, "config.ini")  # 获取config配置文件所在路径


class Readconfig:

    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read(configfile_path)

    def getAppValue(self, name):

        """
            name：'app'下面参数对应的值
        """
        value = self.conf.get('app', name)
        return value

    def getcmdValue(self, name):

        """
            name：'cmd'下面参数对应的值
        """
        value = self.conf.get('cmd', name)
        return value

    def getemailValue(self, name):

        """
            name：'email'下面参数对应的值
        """
        value = self.conf.get('email', name)
        return value

