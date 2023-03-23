"""
# json工具模块

dict <--> 字符串：

+ from_string(json_str: str) -> dict
+ to_string(data: dict, format=False) -> str

和文件互转：

+ from_file(file_path: str, encoding="utf-8") -> dict
+ to_file(file_path: str, data: dict, encoding="utf-8", format=True)

"""

import json


def from_string(json_str: str):
    """ 从字符串中加载json数据
    """

    data = json.loads(json_str)

    return data


def to_string(data: None | int | float | str | list | dict, format=False) -> str:
    """ 将数据转换为json字符串
    """

    if not format:
        json_str = json.dumps(data)
    else:
        json_str = json.dumps(data, ensure_ascii=False, sort_keys=True,
                              indent=4, separators=(',', ':'))

    return json_str


def from_file(file_path: str, encoding="utf-8"):
    """ 从文件中加载json数据
    """

    with open(file_path, 'r', encoding=encoding) as f:
        data = json.load(f)

    return data


def to_file(file_path: str, data: None | int | float | str | list | dict, encoding="utf-8", format=True):
    """ 将数据保存到文件中
    """

    with open(file_path, 'w', encoding=encoding) as f:
        if not format:
            json.dump(data, f)
        else:
            json.dump(data, f, ensure_ascii=False, sort_keys=True,
                      indent=4, separators=(',', ':'))
