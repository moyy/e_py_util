"""
# 字符串编码

+ `to_str(b: bytes, encoding="utf-8") -> str` 将指定编码的 bytes 转换为 str
+ `from_str(s: str, encoding="utf-8") -> bytes` 将 str 转换为指定编码的 bytes

+ `base64_encode(s: str, encoding="utf-8") -> str` 将字符串进行 base64 编码
+ `base64_decode(s: str, encoding="utf-8") -> str` 将字符串进行 base64 解码

+ `base58_encode(s: str, encoding="utf-8") -> str` 将字符串进行 base58 编码
+ `base58_decode(s: str, encoding="utf-8") -> str` 将字符串进行 base58 解码

"""


def to_str(b: bytes, encoding="utf-8") -> str:
    """ 将指定编码的 bytes 转换为 str
    """
    return b.decode(encoding)


def from_str(s: str, encoding="utf-8") -> bytes:
    """ 将 str 转换为指定编码的 bytes"""
    return s.encode(encoding)


def base64_encode(s: str, encoding="utf-8") -> str:
    """ 将字符串进行 base64 编码
    """
    import base64

    b = from_str(s, encoding)

    return base64.b64encode(b).decode(encoding)


def base64_decode(s: str, encoding="utf-8") -> str:
    """ 将字符串进行 base64 解码
    """
    import base64

    b = from_str(s, encoding)

    return base64.b64decode(b).decode(encoding)


def base58_encode(s: str, encoding="utf-8") -> str:
    """ 将字符串进行 base58 编码
    """
    import base58

    b = from_str(s, encoding)

    return base58.b58encode(b).decode(encoding)


def base58_decode(s: str, encoding="utf-8") -> str:
    """ 将字符串进行 base58 解码
    """
    import base58

    b = from_str(s, encoding)

    return base58.b58decode(b).decode(encoding)

# ================= test =================


def _test_to_str():
    b = b"hello world"
    s = to_str(b)
    assert(s == "hello world")


def _test_from_str():
    s = "hello world"
    b = from_str(s)
    assert(b == b"hello world")


def _test_base64_encode():
    s = "hello world"
    e = base64_encode(s)
    assert(e == "aGVsbG8gd29ybGQ=")


def _test_base64_decode():
    e = "aGVsbG8gd29ybGQ="
    s = base64_decode(e)
    assert(s == "hello world")


def _test_base58_encode():
    s = "hello world"
    e = base58_encode(s)
    assert(e == "StV1DL6CwTryKyV")


def _test_base58_decode():
    e = "StV1DL6CwTryKyV"
    s = base58_decode(e)
    assert(s == "hello world")


if __name__ == '__main__':
    _test_to_str()
    _test_from_str()
    _test_base64_encode()
    _test_base64_decode()
    _test_base58_encode()
    _test_base58_decode()

    print("test::encode_util.py::ok!")
