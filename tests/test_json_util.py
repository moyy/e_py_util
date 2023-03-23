
from e_util.json_util import from_string, to_string


def test_dict():
    data = {
        "name": "张三",
        "age": 18,
        "is_man": False,
        "option": None,
        "list": [1, 2, 3, 4, 5],
        "dict": {
            "a": 1,
            "b": 2,
        }
    }

    json_str = to_string(data)
    data_2 = from_string(json_str)

    assert(data == data_2)
    print(f"json_str = {json_str}")
    print(f"data_2 = {data_2}")