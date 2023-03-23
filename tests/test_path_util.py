from e_util.path_util import join_path, parse_path


def test_join_path():
    path = join_path("D:/path_1", "path_2\\", "file.txt")
    assert(path == "D:/path_1/path_2/file.txt")


def test_parse_path():
    info = parse_path("D:/path_1\\path_2/file.txt")

    assert(info["dir"] == "D:/path_1/path_2")
    assert(info["file"] == "file")
    assert(info["extension"] == ".txt")