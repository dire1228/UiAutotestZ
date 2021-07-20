# -*- coding: utf-8 -*-
import json
from utils.logConfig import Log


class ReadConfig(object):
    """
    读取配置文件，Excel、json等文件啊的读取方法可写在此类下边
    """

    def __init__(self):
        self.log = Log().get_log()

    def read_json(self, json_file):
        """读取json文件"""
        try:
            with open(json_file) as f:
                data = json.load(f)
                self.log.debug("json文件：" + str(data))
                return data
        except Exception as e:
            self.log.error("报错了：" + str(e))
            self.log.error("文件不存在或者不是json文件")


if __name__ == '__main__':
    read = ReadConfig()
    read.read_json("../config/base_data.json1")