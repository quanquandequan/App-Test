# coding=utf-8

import os
from common.ReadConfig import Readconfig
from common.logs import Log

conf = Readconfig()
log = Log()


class Devices:

    def __init__(self):

        """
            从config配置文件中获取adb命令
        """

        self.get_device = conf.getadbValue('viewPhone')
        self.get_Version = conf.getadbValue('viewAndroid')

    def get_device_name(self):

        """
            执行adb命令，打印出设备名称
        """

        values = os.popen(self.get_device).readlines()
        dev = values[1].split()[0]
        if len(values)-2 == 1:
            log.info('手机设备为：'+dev)
            return dev
        else:
            log.warn('暂未获取到手机设备')

    def get_platform_version(self):

        """
            执行adb命令，打印出设备版本号
        """

        values = os.popen(self.get_Version).readlines()
        if values != '':
            version = values[0].split()[0]
            log.info('手机版本号为：'+version)
            return version.strip()
        else:
            log.warn('暂未获取到手机设备')


if __name__ == '__main__':
    devices = Devices()
    devices.get_device_name()
    devices.get_platform_version()
