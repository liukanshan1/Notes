a = int(input('输入 a: '))
n = int(input('输入 n: '))
temp = 0
sn = "Sn="  # 表达式的前半部分
s = 0
for i in range(1, n + 1):
    temp = temp * 10 + a
    sn += str(temp)  # 附加temp到表达式中
    sn += "+"  # 附加“+”到表达式中
    s += temp  # 求和

print("表达式为：" + sn[:-1])  # 循环生成的表达式最后一位多了一个”+“，这里输出表达式除最后一位的内容
print("结果为：%d2" % s)
