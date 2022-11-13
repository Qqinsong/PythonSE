# r = map(lambda x: x ** 2, [1, 2, 3, 4, 5])
# print(list(r))

# # 根据绝对值进行排序
# a = sorted([36, 5, -12, 9, -21], key=abs)
# print(a)
#
# # 按照成绩进行排序
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# L1 = sorted(L, key=lambda x: x[1])
# print(L1)

# from functools import reduce
# # 计算1到100的值
# res = reduce(lambda x, y: x + y, range(1, 101))
# print(res)

# 过滤器的用法，过滤掉一个列表中的偶数
def is_odd(n):
    return n % 2 == 1


a = list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 15]))
print(a)

b = list(filter(lambda x: True if x % 2 == 1 else False, [1, 2, 3, 4, 5, 6, 7, 15]))
print(b)


