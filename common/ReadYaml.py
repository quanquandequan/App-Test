# coding=utf-8

import yaml
from common.Logs import Log

log = Log()


class Readyaml:

    """
        读取yaml文件，返回testcase的信息
    """

    def __init__(self, path):

        """
            path：文件路径
        """
        self.path = path

    def read_yaml(self):

        """
            读取yaml文件
        """
        try:
            f = open(self.path, encoding='utf-8')
            data = yaml.load(f)
            f.close()
            return data
        except:
            log.error('未找到yaml文件')

    def alldata(self):
        data = self.read_yaml()
        return data

    def caselen(self):

        """
            获取case的个数
        """
        data = self.alldata()
        length = len(data['testcase'])
        return length

    def get_elementinfo(self, i):

        """
            获取element_info信息
        """
        data = self.alldata()
        return data['testcase'][i]['element_info']

    def get_findtype(self, i):

        """
            获取find_type信息
        """
        data = self.alldata()
        return data['testcase'][i]['find_type']

    def get_operate_type(self, i):

        """
            获取operate_type信息
        """
        data = self.alldata()
        return data['testcase'][i]['operate_type']

    def get_index(self, i):

        """
            获取index信息
        """
        data = self.alldata()
        if self.get_findtype(i) == 'ids':
            return data['testcase'][i]['index']
        else:
            pass

    def get_send_content(self, i):

        """
            获取要输入的内容
        """
        data = self.alldata()
        if self.get_operate_type(i) == 'send_keys':
            return data['testcase'][i]['send_content']
        else:
            pass

    def get_backtimes(self, i):

        """
            获取返回和滑动的次数
        """
        data = self.alldata()
        if self.get_operate_type(i) == 'back':
            return data['testcase'][i]['times']

        elif self.get_operate_type(i) == 'swipe_up':
            return data['testcase'][i]['times']

        elif self.get_operate_type(i) == 'swipe_down':
            return data['testcase'][i]['times']

        elif self.get_operate_type(i) == 'swipe_left':
            return data['testcase'][i]['times']

        elif self.get_operate_type(i) == 'swipe_right':
            return data['testcase'][i]['times']

        elif self.get_operate_type(i) == 'picker_up':
            return data['testcase'][i]['times']

        elif self.get_operate_type(i) == 'picker_down':
            return data['testcase'][i]['times']

        else:
            pass

    def get_title(self):
        data = self.alldata()
        return data['testinfo'][0]['title']

