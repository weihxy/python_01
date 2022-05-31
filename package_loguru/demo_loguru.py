

#loguru模块

"""
1.可以格式化日志
2.着色（不同颜色）
3.生成到文件
4.显示不同的日志级别
5.只使用一个对象（非常方便）
"""
# 1.下载安装

#2，导包：

from loguru import  logger
#3.打印一条日志：helloworld
logger.info("hello world")


#输出不同的日志级别：debug，info，warning，success，error
logger.debug("这是一条debug日志")
logger.info("这是一条info日志")
logger.warning("这是一条warning日志")
logger.success("这是一条success日志")
logger.error("这是一条error日志")

#输出到文件:add(file_name,format,level)
logger.add('a.log',format="{time:YYYY-MM-DD at HH:mm:ss} | {level}| {message} |{module}",level="DEBUG")
logger.debug("这是一条debug日志")
logger.info("这是一条info日志")
logger.warning("这是一条warning日志")
logger.success("这是一条success日志")
logger.error("这是一条error日志")

#传入参数的格式化
logger.info("今天星期{}".1)
logger.info("今天星期{}".format(1))

