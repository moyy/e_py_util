from e_util.encode_util import from_str
from e_util.hash_util import str_md5, bytes_md5

def test_str_md5():
    md5 = str_md5("hello")
    assert(md5 == "5d41402abc4b2a76b9719d911017c592")


def test_bytes_md5():
    blob = from_str("hello")
    md5 = bytes_md5(blob)
    assert(md5 == "5d41402abc4b2a76b9719d911017c592")
