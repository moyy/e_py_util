"""
# 常用的 Hash 函数

+ str_md5(s: str, encoding="utf-8") -> str
+ bytes_md5(blob: bytes) -> str

"""

import hashlib
from encode_util import from_str

def str_md5(s: str, encoding="utf-8") -> str:
    """ 计算字符串的md5，返回 16进制字符串

        Example:
            # md5 = "5d41402abc4b2a76b9719d911017c592"
            md5 = str_md5("hello")
    """

    b = from_str(s, encoding)
    return bytes_md5(b)


def bytes_md5(blob: bytes) -> str:
    """计算二进制数据的md5，返回 16进制字符串
        Example:
            # md5 = "5d41402abc4b2a76b9719d911017c592"
            md5 = bytes_md5("hello".encode("utf-8"))
    """

    md5 = hashlib.md5()

    md5.update(blob)

    return md5.hexdigest()

# ================= test =================


def _test_str_md5():
    md5 = str_md5("hello")
    assert(md5 == "5d41402abc4b2a76b9719d911017c592")


def _test_bytes_md5():
    blob = from_str("hello")
    md5 = bytes_md5(blob)
    assert(md5 == "5d41402abc4b2a76b9719d911017c592")


if __name__ == '__main__':
    _test_bytes_md5()

    _test_str_md5()

    print("test::hash_util.py::ok!")
