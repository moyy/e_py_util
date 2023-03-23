"""
# 目录操作


"""

import os
import shutil
from typing import Iterable
from path_util import join_path


def is_path_exist(path: str) -> bool:
    """ 判断路径是否存在
    """
    return os.path.exists(path)


def make_dir(path: str, exist_ok=True, recursive=True):
    """ 创建目录，参数有 是否递归，存在是否报错
    """
    if recursive:
        os.makedirs(path, exist_ok=exist_ok)
    elif not os.path.exists(path):
        os.mkdir(path)
    else:
        if exist_ok:
            return
        else:
            raise FileExistsError(f"dir already exists, path={path}")


def remove_files(path: str):
    """ 删除 path；如果是目录，递归删除
    """
    shutil.rmtree(path)


def iter_dir(root: str, recursive: bool = True) -> Iterable[str]:
    """ 遍历目录，参数有 是否递归
        returs 路径
    """
    if recursive:
        for root, _, files in os.walk(root):
            for file in files:
                yield join_path(root, file)
    else:
        for file in os.listdir(root):
            yield join_path(root, file)


def read_file_as_str(path: str, encoding="utf-8") -> str:
    """ 读取文件为字符串
    """
    with open(path, 'r', encoding=encoding) as f:
        return f.read()


def write_str_as_file(path: str, content: str, encoding="utf-8"):
    """ 写字符串到文件
    """
    with open(path, 'w', encoding=encoding) as f:
        f.write(content)


def append_str_as_file(path: str, content: str, encoding="utf-8"):
    """ 追加字符串到文件"""
    with open(path, 'a', encoding=encoding) as f:
        f.write(content)


def read_file_as_bytes(path: str) -> bytes:
    """ 读取文件为bytes
    """
    with open(path, 'rb') as f:
        return f.read()


def write_bytes_as_file(path: str, content: bytes):
    """ 写bytes到文件
    """
    with open(path, 'wb') as f:
        f.write(content)


def append_bytes_as_file(path: str, content: bytes):
    """ 追加bytes到文件"""
    with open(path, 'ab') as f:
        f.write(content)

# ================= test =================


def _test_make_dir():
    root_name = "test_dir"
    make_dir(root_name)
    assert(is_path_exist(root_name))

    dir_name = f"{root_name}/test_dir_1/test_dir_2/"
    make_dir(dir_name, exist_ok=True, recursive=True)
    assert(is_path_exist(dir_name))


def _test_remove_dir():
    root_name = "test_dir"
    remove_files(root_name)
    assert(not is_path_exist(root_name))


def _test_file():
    file_name = "test_dir/test_dir_1/test_dir_2/test_file.txt"
    content = "test file"
    write_str_as_file(file_name, content)
    assert(is_path_exist(file_name))

    content = read_file_as_str(file_name)
    assert(content == content)

    expect_content = f"{content}{content}"
    append_str_as_file(file_name, content)
    content = read_file_as_str(file_name)
    assert(content == expect_content)


if __name__ == '__main__':
    _test_make_dir()

    _test_file()

    _test_remove_dir()
