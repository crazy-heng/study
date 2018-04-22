#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from logging import handlers

log_dir = "../logs"


def log(log_name, log_type, log_info):  # 添加记录购物是否成功日志
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.DEBUG)
    fh = handlers.TimedRotatingFileHandler("%s/%s.log" % (log_dir, log_name), when="D", interval=1, backupCount=30,
                                           encoding="utf-8")
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger.addHandler(fh)
    fh.setFormatter(file_formatter)
    if log_type == "error":
        logger.error(log_info)
    elif log_type == "info":
        logger.info(log_info)