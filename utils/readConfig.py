# -*- coding: utf-8 -*-
import json

from utils.logConfig import Log

log = Log("ReadConfig").get_log()


class ReadConfig(object):
    """
    读取配置文件，Excel、json等文件啊的读取方法可写在此类下边
    """

    def read_json(self, json_file):
        """读取json文件"""
        try:
            with open(json_file) as f:
                data = json.load(f)
                log.debug("json文件：" + str(data))
                return data
        except Exception as e:
            log.error("报错了：" + str(e))
            log.error("文件不存在或者不是json文件")


if __name__ == '__main__':
    read = ReadConfig()
    read.read_json("../config/base_data.json")
