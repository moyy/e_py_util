"""
# 路径操作

+ `parse_path(path: str) -> PathInfo` 解析路径
+ `join_path(*paths: str) -> str` 以 / 来 拼接多个路径

"""

import os
from typing import TypedDict


class PathInfo(TypedDict):
    """ 路径信息: 路径，文件名，扩展名
        Example: 
            + path = r"D:/path_1/path_2/file.txt"
            + dir = "D:/path_1/path_2"
            + file = "file"
            + extension = ".txt"
    """
    dir: str
    file: str
    extension: str


def join_path(*paths: str) -> str:
    """ 以 / 来 拼接多个路径

    :param paths: 多个路径
    :return: 拼接后的路径字符串
    """

    # 规范化路径, 并去除路径末尾的"/"
    norm_paths = [os.path.normpath(p).replace("\\", "/").rstrip("/") for p in paths]

    # 拼接路径并返回
    return "/".join(norm_paths)


def parse_path(path: str) -> PathInfo:
    """ 解析路径
    """

    path = os.path.normpath(path)

    file_name = os.path.basename(path)
    file, extension = os.path.splitext(file_name)

    return {
        "dir": os.path.dirname(path).replace("\\", "/"),
        "file": file,
        "extension": extension,
    }
