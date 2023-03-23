from e_util.encode_util import to_str, from_str, base64_encode, base64_decode, base58_encode, base58_decode


def test_to_str():
    b = b"hello world"
    s = to_str(b)
    assert(s == "hello world")


def test_from_str():
    s = "hello world"
    b = from_str(s)
    assert(b == b"hello world")


def test_base64_encode():
    s = "hello world"
    e = base64_encode(s)
    assert(e == "aGVsbG8gd29ybGQ=")


def test_base64_decode():
    e = "aGVsbG8gd29ybGQ="
    s = base64_decode(e)
    assert(s == "hello world")


def test_base58_encode():
    s = "hello world"
    e = base58_encode(s)
    assert(e == "StV1DL6CwTryKyV")


def test_base58_decode():
    e = "StV1DL6CwTryKyV"
    s = base58_decode(e)
    assert(s == "hello world")