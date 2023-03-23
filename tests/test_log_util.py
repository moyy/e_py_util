
import logging
from e_util.log_util import get_logger


def test_default_log():
    # 默认日志，不会打印到控制台，只会输出到文件
    default_logger = get_logger(logging.INFO, "run.log")

    default_logger.info("default_logger, info")

    # 这条不会输出，因为level是INFO
    default_logger.debug("default_logger, debug")


def test_category_log():
    # category日志，会打印到控制台，也会输出到文件
    category_logger = get_logger(logging.DEBUG, "category.log", "category")

    category_logger.debug("category_logger, debug")
