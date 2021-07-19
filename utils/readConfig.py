# -*- coding: utf-8 -*-
import json
import logging


class ReadConfig(object):
    """
    读取配置文件，Excel、json等文件啊的读取方法可写在此类下边
    """

    def __init__(self):
        pass

    @staticmethod
    def read_json(json_file):
        """读取json文件"""
        try:
            with open(json_file) as f:
                data = json.load(f)
                return data
        except Exception as e:
            print(e)
            print("文件不存在或者不是json文件")
