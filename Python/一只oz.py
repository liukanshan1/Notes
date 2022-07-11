print("欢迎进入一只oz的世界")
Message1=True
while Message1:
    Date=input("一只oz的生日:")
    if Date=="10月24日":
        print("正确")
        Message1=False
    else:
        print("错误")
print("恭喜你，离一只oz近了一步！")
print("接招！！")
Message2=True
while Message2:
    num=input("一只oz有过几个对象:")
    Sum=int(num)
    if Sum==0:
        print("离一只oz又近了一步")
        Message2=False
    else:
        print("我讨厌你！")
print("看来你已经可以成为我的好基友了！")