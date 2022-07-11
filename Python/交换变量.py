# 用户输入

x = input('输入 x 值: ')
y = input('输入 y 值: ')

# 创建临时变量，并交换
temp = x
x = y
y = temp

print('交换后 x 的值为: {}'.format(x))
print('交换后 y 的值为: {}'.format(y))
#format用法

#我们也可以不创建临时变量，用一个非常优雅的方式来交换变量：
x,y = y,x
print('交换后 x 的值为: {}'.format(x))
print('交换后 y 的值为: {}'.format(y))