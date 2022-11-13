# 简单选择排序
def SelectSort(nums):
    for i in range(len(nums)):
        temp = nums[i]
        for j in range(i + 1, len(nums)):
            if nums[j] < temp:
                temp = nums[j]  # 寻找最小值
                flog_j = j   # 记录交换的位置

        sub = nums[i]   # 按位置进行交换
        nums[i] = temp
        nums[flog_j] = sub


a = [7, 6, 1, 2, 3]
print("排序前:")
print(a)
SelectSort(a)
print("排序后:")
print(a)
