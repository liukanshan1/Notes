#方法一
def clone_runoob(li1):
    li_copy = li1[:]
    return li_copy
li1 = [4, 8, 2, 10, 15, 18]
li2 = clone_runoob(li1)
print("原始列表:", li1)
print("复制后列表:", li2)


#方法二：使用extend()
def clone_runoob(li1):
    li_copy = []
    li_copy.extend(li1)
    return li_copy
li1 = [4, 8, 2, 10, 15, 18]
li2 = clone_runoob(li1)
print("原始列表:", li1)
print("复制后列表:", li2)


#方法三：使用list()
def clone_runoob(li1):
    li_copy = list(li1)
    return li_copy
li1 = [4, 8, 2, 10, 15, 18]
li2 = clone_runoob(li1)
print("原始列表:", li1)
print("复制后列表:", li2)