# Write-up

## check in

题目里提示flag in rules，于是去rules界面找到flag：

`Kap0k{this_is_a_sample_flag}`

## 点击

下载`click.zip`，运行其中的执行文件。使用鼠标连点器，得到flag：

`Kap0k{amaz1ng_y0u_d1d_1t}`

## 歪比巴卜

使用[戴夫编码解密工具](https://cloud.jeffz.cn/websites/daifu/)，输入密文，得到flag：

`Kap0k{daifu_encode_the_flag}`

## 藏了东西

下载题目的压缩包并解压，使用010 Editor打开，发现文件头是`50 4B 03 04`，对应zip压缩包。然后改文件后缀名为`.zip`并解压，得到一个视频文件和一个文本文档。文本文档的内容是莫斯密码，解密后得到了一串用核心价值观编码的字符串，使用核心价值观编码解密......

## Just a ^

题目为异或加密，观察acsii码得到密钥“8”，使用异或解密得到flag：

`Kap0k{Single_byte_xor}`

