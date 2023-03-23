from e_util.file_util import append_str_as_file, is_path_exist, make_dir, remove_files, read_file_as_str, write_str_as_file


def test_file():
    root_name = "test_dir"
    make_dir(root_name)
    assert(is_path_exist(root_name))

    dir_name = f"{root_name}/test_dir_1/test_dir_2/"
    make_dir(dir_name, exist_ok=True, recursive=True)
    assert(is_path_exist(dir_name))

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

    remove_files(root_name)
    assert(not is_path_exist(root_name))
