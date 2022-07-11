## CTF工具

1. [摩斯编码](http://www.zhongguosou.com/zonghe/moErSiCodeConverter.aspx)

2. 敲击码

​       敲击码（Tap code）是一种以非常简单的方式对文本信息进行编码的方法。因该编码对信息通过使用一系列的点击声音来编码而命名， K 字母被整合到 C 中。

|Tap Code|1|2|3|4|5|
| ---- | ---- | ---- | ---- | ---- | ---- |
|1|A|B|C/K|D|E|
|2|F|G|H|I|J|
|3|L|M|N|O|P|
|4|Q|R|S|T|U|
|5|V|W|X|Y|Z|


3. [曼彻斯特编码](https://zh.wikipedia.org/wiki/%E6%9B%BC%E5%BD%BB%E6%96%AF%E7%89%B9%E7%BC%96%E7%A0%81)

4. [格雷码](https://zh.wikipedia.org/wiki/%E6%A0%BC%E9%9B%B7%E7%A0%81)

5. [ASCII](http://www.ab126.com/goju/1711.html)

   ![ascii](http://ctfwiki.ycdxsb.cn/misc/encode/figure/ascii.jpg)

6. [base编码](http://www1.tc711.com/tool/BASE64.htm)

   - base64 结尾可能会有 `=` 号，但最多有 2 个
   - base32 结尾可能会有 `=` 号，但最多有 6 个
   - base64 编码的字符长度刚好是3的倍数时，编码后的字符串末尾不会出现 `=` 号。
   - 根据 base 的不同，字符集会有所限制
   - **有可能需要自己加等号**
   - **= 也就是 3D**

7. [base64隐写工具](https://github.com/cjcslhp/wheels/tree/master/b64stego)

   使用脚本读取隐写信息。

   ```Python
   import base64
   
   def deStego(stegoFile):
       b64table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
       with open(stegoFile,'r') as stegoText:
           message = ""
           for line in stegoText:
               try:
                   text = line[line.index("=") - 1:-1]
                   message += "".join([ bin( 0 if i == '=' else b64table.find(i))[2:].zfill(6) for i in text])[2 if text.count('=') ==2 else 4:6]  
               except:
                   pass
       return "".join([chr(int(message[i:i+8],2)) for i in range(0,len(message),8)])
   
   print(deStego("text.txt"))
   ```

8. [霍夫曼编码](https://zh.wikipedia.org/wiki/%E9%9C%8D%E5%A4%AB%E6%9B%BC%E7%BC%96%E7%A0%81)

9. [质因数分解](https://zh.numberempire.com/numberfactorizer.php)

10. [XXencoding](http://web.chacuo.net/charsetxxencode)

   特点

   - 只有数字，大小写字母
   - \+ 号，- 号。

11. URL编码

    特点：大量的百分号

12. Unicode编码

    四种表现形式：

    - 源文本： `The`
    -  &#x [Hex]: `The`
    - &# [Decimal]: `The`
    -   \U [Hex]: `\U0054\U0068\U0065`
    -   \U+ [Hex]: `\U+0054\U+0068\U+0065`

13. [条形码](https://online-barcode-reader.inliteresearch.com/)

14. 二维码

    - 用某种特定几何图形按一定规律在平面分步的黑白相间的图形记录数据符号信息

    - 堆叠式 / 行排式二维码：Code 16 k、Code 49、PDF417

    - 矩阵式二维码：QR CODE

      ![img](http://ctfwiki.ycdxsb.cn/misc/encode/figure/qr1.jpg)![img](http://ctfwiki.ycdxsb.cn/misc/encode/figure/qr2.jpg)
      
 15. [PCAP文件修复](https://f00l.de/hacking/pcapfix.php)
      
    详细内容见PDF文件
    
 16. [凯撒密码](https://quipqiup.com/)

 17. [分解整数](http://factordb.com/)

 18. [MD5破解](http://www.cmd5.com/)
     [MD5破解](http://www.ttmd5.com/)
     [MD5破解](http://pmd5.com/)
     [生成指定前缀的 md5 碰撞](https://www.win.tue.nl/hashclash/fastcoll_v1.0.0.5.exe.zip)

 19. [brainfuck](http://bf.doleczek.pl/)
     [brainfuck&Ook!](https://www.splitbrain.org/services/ook)
       [介绍](https://baike.baidu.com/item/Brainfuck/1152785?fr=aladdin)

 20. uuencode编码特征：特殊符号很多。

 21. xxencode末尾使用的补全符号为 `+` 

 22. jjencode和aaencode：前者是将JS代码转换成只有符号的特殊字符串，后者是将JS代码转换成常用的网络表情，本质上是对JS代码的一种混淆。

 23. [维吉尼亚密码](https://atomcated.github.io/Vigenere)

 24. PNG文件以 `89 50 4E 0D 0A 1A 0A` 开始，以 `00 00 00 00 49 45 4E AE 42 60 82` 作为结束。

 25. [盲水印](https://github.com/chishaxie/BlindWaterMark)

 26. ZIP伪加密：目录区头 `50 4B 01 02` 偏移8字节，其本身占2字节，最低位表示这个文件是否被加密。

 27. 文件头

 |文件类型|文件头|文件尾|
| ---- | ---- | ---- |
|JPEG/JPG|FF D8 FF|FF D9|
|PNG|89 50 4E 47|AE 42 60 82|
|GIF|47 49 46 38|00 3B|
|ZIP|50 4B 03 04|50 4B|
|RAR|52 61 72 21| |
|WAV|57 41 56 45| |    
|AVI|41 56 49 20| |
|MPEG|00 00 01 BA| |
|MPEG|00 00 01 B3| |
|MOV|6D 6F 6F 76| |