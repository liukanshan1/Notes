# Forensic Steganography

### `file` 命令

`file` 命令根据文件头（魔法字节）去识别一个文件的文件类型。

```
root in ~/Desktop/tmp λ file flag
flag: PNG image data, 450 x 450, 8-bit grayscale, non-interlaced
```

### `strings` 命令

打印文件中可打印的字符，经常用来发现文件中的一些提示信息或是一些特殊的编码信息，常常用来发现题目的突破口。

- 可以配合 `grep` 命令探测指定信息

  ```
  strings test|grep -i XXCTF
  ```

- 也可以配合 `-o` 参数获取所有 ASCII 字符偏移

  ```
  root in ~/Desktop/tmp λ strings -o flag|head
      14 IHDR
      45 gAMA
      64  cHRM
      141 bKGD
      157 tIME
      202 IDATx
      223 NFdVK3
      361 |;*-
      410 Ge%<W
      431 5duX@%
  ```

### `binwalk` 命令 

binwalk 本是一个固件的分析工具，比赛中常用来发现多个文件粘合再在一起的情况。根据文件头去识别一个文件中夹杂的其他文件，有时也会存在误报率（尤其是对 Pcap 流量包等文件时）。

```
root in ~/Desktop/tmp λ binwalk flag

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 450 x 450, 8-bit grayscale, non-interlaced
134           0x86            Zlib compressed data, best compression
25683         0x6453          Zip archive data, at least v2.0 to extract, compressed size: 675, uncompressed size: 1159, name: readme.txt
26398         0x671E          Zip archive data, at least v2.0 to extract, compressed size: 430849, uncompressed size: 1027984, name: trid
457387        0x6FAAB         End of Zip archive
```

配合 `-e` 参数可以进行自动化提取。

也可以结合 `dd` 命令进行手动切割。

```
root in ~/Desktop/tmp λ dd if=flag of=1.zip bs=1 skip=25683
431726+0 records in
431726+0 records out
431726 bytes (432 kB, 422 KiB) copied, 0.900973 s, 479 kB/s
```

