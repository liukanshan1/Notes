def _sum(arr, n):
    # 使用内置的 sum 函数计算
    return (sum(arr))


# 调用函数
arr = []
# 数组元素
arr = [12, 3, 4, 15]

# 计算数组元素的长度
n = len(arr)

ans = _sum(arr, n)

# 输出结果
print('数组元素之和为', ans)