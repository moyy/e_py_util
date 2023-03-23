"""
# 日志模块

+ get_logger(name: str = "", level: int = logging.INFO, file_path: Optional[str] = None) -> logging.Logger

"""

import sys
import logging

from typing import Optional

# 保存已经创建的logger
_loggers: dict[str, logging.Logger] = {}


def get_logger(level: int = logging.INFO, file_path: Optional[str] = None, name: str = "") -> logging.Logger:
    """
    Description:
        通过name取到日志，不存在就创建一个返回。
        总是输出到控制台；file_path 不为空，还会输出到文件。

    Example:
        # 默认日志，不会打印到控制台，只会输出到文件
        default_logger = get_logger("", logging.INFO, "run.log")
        default_logger.info("default_logger, info")
        default_logger.debug("default_logger, debug")

        # category日志，会打印到控制台，也会输出到文件
        category_logger = get_logger("category", logging.DEBUG)
        category_logger.debug("category_logger, debug")
    """

    if name not in _loggers:
        _loggers[name] = _Logger(level, file_path, name).logger

    return _loggers[name]


class _Logger:
    """ 日志类
    """

    def __init__(self, level: Optional[int] = logging.INFO, file_path: Optional[str] = None, name: str = ""):
        """ 初始化
            Args:
                name: logger name
                level: logger level
                log_path: log file path
        """

        level = level if level else logging.INFO

        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.logger.handlers.clear()

        self._add_console_handler(level)

        if file_path:
            self._add_file_handler(level, file_path)

    def _add_console_handler(self, level: int):

        # 例子 [2023-03-23 11:55:16,391] [category] [DEBUG]: category_logger, debug
        formatter = logging.Formatter(
            '[%(asctime)s] [%(name)s] [%(levelname)s]: %(message)s')

        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(level)
        ch.setFormatter(formatter)

        self.logger.addHandler(ch)

    def _add_file_handler(self, level: int, file_path: str):

        # 例子 [2023-03-23 15:14:30,966] [pid:20244 / tid:2120(MainThread)] [root] [INFO]: default_logger, info
        formatter = logging.Formatter(
            '[%(asctime)s] [pid:%(process)d / tid:%(thread)d(%(threadName)s)] [%(name)s] [%(levelname)s]: %(message)s')

        fh = logging.FileHandler(file_path, encoding='utf-8')
        fh.setLevel(level)
        fh.setFormatter(formatter)

        self.logger.addHandler(fh)
