#第一种实现方式
def Reverse(lst):
    return [ele for ele in reversed(lst)]


lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))

#第二种实现方式
def Reverse(lst):
    lst.reverse()
    return lst

lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))

#第三种实现方式
def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst

lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))

#第四种实现方式
#还可以直接调用 list 列表的 sort 方法, 设置 reverse 为 True 即可翻转列表：

li = [*range(10, 16)]
# 得到列表 li = [10, 11, 12, 13, 14, 15], * 为解包符号
print(li)

# 降序排列
li.sort(reverse = True)
print(li)
# 输出: [15, 14, 13, 12, 11, 10]

#第五种实现方式
def fanzhuan(list):
    a=[]
    i=len(list)
    while i>0:
         a.append(list[i-1]) #生成一个新的列表，原列表的最后一位成为第一位
         i-=1 #依次向前进一位
    return a
fa=fanzhuan([34,12,54,234,65,122])
print(fa)