str1 = input("请输入句子：")
list1 = str1.split()
length = 0
for i in list1:
    if length < len(i):
        length = len(i)
print("最长的单词长度为：%d" % length)
print("最长的单词：", end='')
for i in list1:
    if length == len(i):
        print(i, end=' ')