## flush
python的print（flush=True）实现动态Loading......效果

```Python
import time                                                                           
print("Loading",end = "")
for i in range(6):
    print(".",end = '')
    time.sleep(0.2)
```

想用以上代码实现在Loading同一行后面每0.2秒输出1个点号，总共6个。

可是上面代码效果是；6x0.2秒后1次性输出Loading……

问题出在：上面那样循环会堵塞输出,要等sleep全部执行完,才一并打印出全部结果。要在for循环里面的end = ""后面加上flush = True，即：

```Python

import time                                                                           
print("Loading",end = "")
for i in range(6):
    print(".",end = '',flush = True)
    time.sleep(0.2)
```

再举个例子：
我们知道print也可输出到文件。在python3 交互模式中输入：

```Python
f = open("123.txt", "w")
print("123456789", file = f)
```

运行后打开123.txt文件，发现“123456789”未被写入，文件内容为空。只有f.close()后才将内容写进文件中。如果加入flush = True，即上面代码改为：

```Python
f = open("123.txt", "w")
print("123456789",file = f, flush = True)
```

不用f.close()即可将内容写进文件中。

flush参数主要是刷新， 默认flush = False，不刷新，如上面例子，print到f中的内容先存到内存中，当文件对象关闭时才把内容输出到 123.txt 中；而当flush = True时它会立即把内容刷新存到 123.txt 中。
