# e_py_util

Python Util Package

## 安装

``` bat

 pip3 install git+https://github.com/moyy/e_py_util.git
 
```

## 模块 功能

+ `encode_util` 编码工具，主要有：字符串编码/解码，Base64编码/解码，Base58编码/解码
+ `file_util` 文件工具，主要有：判断路径存在，创建/删除/迭代目录，读/写/追加 字符串/二进制 到 文件
+ `hash_util` 哈希工具，主要有：计算字符串/二进制 的 MD5 哈希值
+ `json_util` JSON 工具，主要有：读/写 JSON 文件，读/写 JSON 字符串
+ `log_util` 日志工具，主要有：日志输出到控制台，日志输出到文件
+ `path_util` 路径工具，主要有：解析路径，合并路径

## 测试 pytest

安装: pip3 install pytest

+ 测试文件以 test_ 开头
+ 测试类 以 Test 开头，并且不能带有 __init__ 方法
+ 测试函数 以 test_ 开头

``` bat

pytest tests/

```