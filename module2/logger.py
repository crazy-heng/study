#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from logging import handlers


class IgnoreBackupLogFilter(logging.Filter):  # filter过滤日志
    """忽略带db backup 的日志"""
    def filter(self, record):  # 固定写法
        return "db backup" not in record.getMessage()


# 1 生成logger对象,默认全局日志级别info
logger = logging.getLogger("web")
logger.setLevel(logging.DEBUG)

# 1.1过滤绑定到logger
logger.addFilter(IgnoreBackupLogFilter())

# 2 生成handler对象，要level生效需要全局日志界别为Debug，不然会被默认全局info过滤掉
ch = logging.StreamHandler()
# ch.setLevel(logging.INFO)
# fh = logging.FileHandler("web.log")
# fh.setLevel(logging.WARNING)
fh = handlers.RotatingFileHandler("web.log", maxBytes=1000, backupCount=3)  # 按大小截断日志
# fh = handlers.TimedRotatingFileHandler("web.log", when="S", interval=5, backupCount=3)  # 按时间截断日志

# 2.1 把handler对象绑定到logger
logger.addHandler(ch)
logger.addHandler(fh)

# 3 生成formatter对象
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(lineno)s - %(message)s')

# 3.1 把formatter对象绑定到
ch.setFormatter(console_formatter)
fh.setFormatter(file_formatter)


logger.debug("test log debug")
logger.info("test log info")
logger.error("test log error")
logger.error("test log error db backup")