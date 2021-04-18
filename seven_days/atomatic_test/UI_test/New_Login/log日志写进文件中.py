#coding=utf-8
import logging


# 定义文件
logFile = logging.FileHandler('logTest.txt', 'a', encoding='utf-8')

# 设置log日志格式
fmt = logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s')
logFile.setFormatter(fmt)

# 定义log日志级别
logger = logging.Logger('logTest', level=logging.DEBUG)
logger.addHandler(logFile)

logger.info("======log日志终于可以用了======")
logger.info("======开始使用log日志======")