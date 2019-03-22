import logging
import os.path
import time


class Logger(object):
    """
    指定保存日志的文件路径，日志级别以及调用文件
    """
    def __init__(self, logger):
        #创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        #