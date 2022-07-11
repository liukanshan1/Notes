# 初始化列表
test_list_set = [1, 6, 3, 5, 3, 4]
test_list_bisect = [1, 6, 3, 5, 3, 4]

print("查看 4 是否在列表中 ( 使用 set() + in) : ")

test_list_set = set(test_list_set)
if 4 in test_list_set:
    print("存在")

print("查看 4 是否在列表中 ( 使用 count()) : ")

if test_list_bisect.count(4) > 0:
    print("存在")