## Python 操作二进制数据

1. struct 模块

有的时候需要用 Python 处理二进制数据，比如，存取文件，socket 操作时。这时候，可以使用 Python 的 struct 模块来完成。

struct 模块中最重要的三个函数是`pack()`、`unpack()`和`calcsize()`

- `pack(fmt, v1, v2, ...)`按照给定的格式（fmt），把数据封装成字符串（实际上是类似于 c 结构体的字节流）
- `unpack(fmt, string)`按照给定的格式（fmt）解析字节流 string，返回解析出来的 tuple
- `calcsize(fmt)` 计算给定的格式（fmt）占用多少字节的内存

这里打包格式`fmt`确定了将变量按照什么方式打包成字节流，其包含了一系列的格式字符串。这里就不再给出不同格式字符串的含义了，详细细节可以参照 Python Doc

```python
>>> import struct
>>> struct.pack('>I',16)
'\x00\x00\x00\x10'
```

`pack`的第一个参数是处理指令，`'>I'`的意思是：`>`表示字节顺序是 Big-Endian，也就是网络序，`I` 表示 4 字节无符号整数。

后面的参数个数要和处理指令一致。

读入一个 BMP 文件的前 30 字节，文件头的结构按顺序如下

- 两个字节：`BM` 表示 Windows 位图，`BA` 表示 OS/2 位图
- 一个 4 字节整数：表示位图大小
- 一个 4 字节整数：保留位，始终为 0
- 一个 4 字节整数：实际图像的偏移量
- 一个 4 字节整数：Header 的字节数
- 一个 4 字节整数：图像宽度
- 一个 4 字节整数：图像高度
- 一个 2 字节整数：始终为 1
- 一个 2 字节整数：颜色数

```python

>>> import struct
>>> bmp = '\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
>>> struct.unpack('<ccIIIIIIHH',bmp)
('B', 'M', 691256, 0, 54, 40, 640, 360, 1, 24)
```
bytearray 字节数组 
将文件以二进制数组形式读取

```python
data = bytearray(open('challenge.png', 'rb').read())
```
字节数组就是可变版本的字节

```python
data[0] = '\x89'
```
