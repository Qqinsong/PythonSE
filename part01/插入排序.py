def insertSort(nums):
    for i in range(1, len(nums)):
        temp = nums[i]  # 要插入的元素
        j = i - 1  # 从前一个位置开始比较
        while j >= 0 and nums[j] > temp:
            nums[j + 1] = nums[j]  # 如果大于temp的值向后移
            j -= 1
        nums[j + 1] = temp  # 赋值新的元素


a = [7, 6, 1, 2, 3]
print("排序前:")
print(a)
insertSort(a)
print("排序后:")
print(a)