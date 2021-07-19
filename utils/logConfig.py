# -*- coding: utf-8 -*-

import logging
import colorlog
import datetime
import os


class Log:


    def __init__(self):
        self.log_colors_config = {
            'DEBUG': 'white',  # cyan white
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'bold_red',
        }

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        # 以时间命名log文件
        base_path = os.path.dirname(os.path.abspath(__file__))
        file_name = datetime.datetime.now().strftime("%Y-%m-%d") + '.log'
        log_name = base_path + '\\..\\log\\' + file_name

        # 日志输出格式
        file_formatter = logging.Formatter(
            fmt='[%(asctime)s.%(msecs)03d] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s',
            datefmt='%Y-%m-%d  %H:%M:%S'
        )
        console_formatter = colorlog.ColoredFormatter(
            fmt='%(log_color)s[%(asctime)s.%(msecs)03d] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s',
            datefmt='%Y-%m-%d  %H:%M:%S',
            log_colors=self.log_colors_config
        )

        # 将日志写入磁盘
        self.file_handler = logging.FileHandler(log_name, 'a', encoding='utf-8')
        self.file_handler.setLevel(logging.DEBUG)
        self.file_handler.setFormatter(file_formatter)
        self.logger.addHandler(self.file_handler)

        # 日志打印
        self.console_handler = logging.StreamHandler()
        self.console_handler.setFormatter(console_formatter)
        self.console_handler.setLevel(logging.DEBUG)
        self.logger.addHandler(self.console_handler)

        self.console_handler.close()
        self.file_handler.close()



    def log(self):
        """获取log"""
        return self.logger

    def close_handle(self):
        """关闭handle"""
        self.logger.removeHandler(self.file_handler)
        self.file_handler.close()


if __name__ == '__main__':
    a = Log()
    a.log().debug("debug log")
    a.log().info("info log")
    a.log().warning("warning log")
    a.log().critical("critical log")
    # a.close_handle()
